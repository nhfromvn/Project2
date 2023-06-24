from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'student.class'
    name = fields.Char()
    size = fields.Integer()
    teacher = fields.Many2one('teacher')
