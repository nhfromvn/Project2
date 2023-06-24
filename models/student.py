from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    name = fields.Char()
    student_class = fields.Many2one('student.class')

