from odoo import models, fields, api


class SubjectInfo(models.Model):
    _name = 'subject.info'
    subject = fields.Many2one('subject')
    semester = fields.Integer()
    type = fields.Char('')
    score = fields.Float('')
    multiplier = fields.Integer('')

