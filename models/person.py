from odoo import models, fields, api


class Person(models.Model):
    _name = 'person'
    first_name = fields.Char()
    middle_name = fields.Char()
    last_name = fields.Char()
    age = fields.Integer()
    dob = fields.Date()
    gender = fields.Boolean()
    email = fields.Char()
    address = fields.Char(default='Ktx Bach khoa')
    religion = fields.Char(default='Không')
    ethnicity = fields.Char(defaut='Kinh')
    job = fields.Char()
    literacy = fields.Char(default='Thạc sỹ')
    image_url = fields.Char()
    phone = fields.Char(default='0123456897')
