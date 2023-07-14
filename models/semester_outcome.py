from odoo import models, fields, api


class SemesterOutcome(models.Model):
    _name = 'semester.outcome'
    student = fields.Many2one('student')
    semester = fields.Integer()
    conduct = fields.Char()
    academic_ability= fields.Char()