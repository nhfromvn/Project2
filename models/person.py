from odoo import models, fields, api


class Person(models.Model):
    _name = 'person'
    name = fields.Char()
    age = fields.Integer()
    email = fields.Char()
    address = fields.Char()
    religion = fields.Char()
    ethnicity = fields.Char()
    job = fields.Char()
    literacy = fields.Char()

