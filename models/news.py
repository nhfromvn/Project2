from odoo import models, fields, api


class News(models.Model):
    _name = 'news'
    title = fields.Char()
    description = fields.Char()
    content = fields.Char()
    start_time = fields.Date()
    end_time = fields.Date()
    image_url = fields.Char()
