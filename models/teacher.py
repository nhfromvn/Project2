from odoo import models, fields, api
from . import person


class Teacher(models.Model):
    _name = 'teacher'
    _inherit = 'person'
    working_time = fields.Integer()
    office_subject = fields.Many2one('office.subject')
    user = fields.Many2one('res.users')
    main_teacher = fields.Boolean(default=False)
    student_class = fields.Many2one('student.class')
