from odoo import models, fields, api


class Subject(models.Model):
    _name = 'subject'
    name = fields.Char()
    teacher = fields.Many2one('teacher')
    student = fields.Many2one('student')
    subject_infos = fields.One2many('subject.info', 'subject')
