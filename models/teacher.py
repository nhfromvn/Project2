from odoo import models, fields, api


class Teacher(models.Model):
    _name = 'teacher'
    name = fields.Char()
