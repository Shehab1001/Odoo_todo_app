from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
    _name = "todo.task"
    _description = "Todo Task App"
    _rec_name = "task_name"

    task_name = fields.Char()
    assign_to = fields.Char()
    description = fields.Char()
    due_date = fields.Date()
    estimated_time = fields.Integer()
    total_time = fields.Integer(compute='_compute_total_time', store=True)
    active = fields.Boolean(default=True)
    is_late = fields.Boolean(default=False)
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('closed', 'Closed'),
    ])

    timesheet_ids = fields.One2many('timesheet.line', 'task_id')

    @api.depends('timesheet_ids.total_time')
    def _compute_total_time(self):
        for rec in self:
            rec.total_time = sum(rec.timesheet_ids.mapped('total_time'))

    @api.constrains('timesheet_ids', 'estimated_time')
    def check_time(self):
        for rec in self:
            if rec.estimated_time and rec.total_time > rec.estimated_time:
                raise ValidationError('Time exceeded')

    def check_due_date(self):
        task_ids = self.search([])
        for rec in task_ids:
            if rec.due_date and fields.Date.today() > rec.due_date:
                rec.is_late = True

    def action_close(self):
        for rec in self:
            rec.status = 'closed'


class TimesheetLine(models.Model):
    _name = "timesheet.line"
    _description = "Timesheet Line"

    description = fields.Char()
    total_time = fields.Integer()
    task_id = fields.Many2one('todo.task')