from odoo import models, fields, api
from . import person


class Student(models.Model):
    _name = 'student'
    _inherit = 'person'
    student_class = fields.Many2one('student.class')
    user = fields.Many2one('res.users')
