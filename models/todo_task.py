from odoo import models, fields, api


class TodoTask(models.Model):
    _name = "todo.task"
    _description = "Todo Task App"
    task_name = fields.Char()
    assign_to = fields.Char()
    description = fields.Char()
    due_date = fields.Date()
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ])
