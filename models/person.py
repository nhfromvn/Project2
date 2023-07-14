from odoo import models, fields, api


class Person(models.Model):
    _name = 'person'
    first_name = fields.Char()
    middle_name = fields.Char(default='Văn')
    last_name = fields.Char()
    age = fields.Integer()
    dob = fields.Date(default=lambda self: fields.Datetime.now())
    gender = fields.Boolean()
    email = fields.Char()
    address = fields.Char(default='Ktx Bach khoa')
    religion = fields.Char(default='Không')
    ethnicity = fields.Char(defaut='Kinh')
    job = fields.Char()
    literacy = fields.Char(default='Thạc sỹ')
    image_url = fields.Char()
    phone = fields.Char(default='0123456897')
