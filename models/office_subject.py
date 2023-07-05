from odoo import models, fields, api


class OfficeSubject(models.Model):
    _name = 'office.subject'
    name = fields.Char()
    office = fields.Char()
    num_teacher = fields.Integer()
    teachers = fields.Many2many('teacher')
