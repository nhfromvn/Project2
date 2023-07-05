from odoo import models, fields, api


class LearningOutcome(models.Model):
    _name = 'learning.outcome'
    student = fields.Many2one('student')
    mark = fields.Float()
    academic_ability = fields.Char()
    conduct = fields.Char()
    semester = fields.Integer()
