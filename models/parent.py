from odoo import models, fields, api


class Parent(models.Model):
    _name = 'parent'
    student = fields.Many2one('student')
    relationship = fields.Char()
