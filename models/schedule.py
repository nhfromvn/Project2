from odoo import models, fields, api


class Schedule(models.Model):
    _name = 'schedule'
    class_time = fields.Integer()
    student_class = fields.Many2one('student.class')
    subject = fields.Char()
    teacher = fields.Many2one('teacher')
    date_of_week = fields.Integer()
    semester = fields.Integer()
    classroom = fields.Char()
