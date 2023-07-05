from odoo import models, fields, api


class ResUsers(models.Model):
    _inherit = 'res.users'
    role = fields.Selection([('student', 'Student'),
                             ('teacher', 'Teacher'),
                             ('cadre', 'Cadre'),
                             ('admin', 'Admin')], default='student')
    image_url = fields.Char('/thpt/static/app/img/Anh-meo-cute-dang-yeu-de-thuong.jpg')

