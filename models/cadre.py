from odoo import models, fields, api
from . import person


class Cadre(models.Model):
    _name = 'cadre'
    _inherit = 'person'
    working_time = fields.Integer()
    team_in_charge = fields.Char()
    user = fields.Many2one('res.users')
