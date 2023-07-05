from odoo import models, fields, api


class SubjectInfo(models.Model):
    _name = 'subject.info'
    name = fields.Char()
    subject = fields.Many2one('subject')
    semester = fields.Integer()
    type = fields.Char('')
    mark = fields.Float('')
    multiplier = fields.Integer('')

