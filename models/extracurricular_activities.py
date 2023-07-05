from odoo import models, fields, api


class ExtracurricularActivities(models.Model):
    _name = 'extracurricular.activities'
    teacher_in_charge = fields.Many2one('teacher')
    teachers = fields.Many2many()
    time = fields.Integer()
    description = fields.Char()
    location = fields.Char()
    start_time = fields.Datetime()
    end_time = fields.Datetime()
    max_participants = fields.Integer()
    participants = fields.Integer()
    semester = fields.Char()
    content = fields.Char()
