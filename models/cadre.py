from odoo import models, fields, api


class Cadre(models.Model):
    _name = 'cadre'
    working_time = fields.Integer()
    team_in_charge = fields.Char()

