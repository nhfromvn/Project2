from odoo import models, fields, api


class ExtracurricularActivities(models.Model):
    _name = 'extracurricular.activities'
    teacher_in_charge = fields.Many2one('teacher')
    title= fields.Char()
    time = fields.Integer()
    description = fields.Char()
    location = fields.Char()
    start_time = fields.Datetime()
    end_time = fields.Datetime()
    max_participants = fields.Integer()
    participants = fields.One2many('student', 'extracurricular_activitie')
    semester = fields.Integer()
    content = fields.Char()
    support_teacher1 = fields.Many2one('teacher')
    support_teacher2 = fields.Many2one('teacher')
    support_teacher3 = fields.Many2one('teacher')
