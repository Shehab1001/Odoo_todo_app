{
    "name": "To-Do List",
    "version": "17.0.0.1.0",
    "author": "Shehab Saeed",
    "application": True,
    "data": [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_view.xml',
        'reports/todo_report.xml'

    ],
    "depends": ["base"],
    "assets": {
            "web.assets_backend" : ["todo_management/static/css/todo.css"]
    }
}