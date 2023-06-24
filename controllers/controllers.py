# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import jinja2
import os
import json

path = os.path.realpath(os.path.join(os.path.dirname(__file__), '../static/src/html'))
loader = jinja2.FileSystemLoader(path)
jinja_env = jinja2.Environment(loader=loader, autoescape=True)
jinja_env.filters["json"] = json.dumps


class Thpt(http.Controller):
    @http.route('/thpt', auth='user')
    def index(self, **kw):
        return request.render('thpt.test')

    @http.route('/map', auth='public', website=True)
    def map(self, **kw):
        template = jinja_env.get_template('index.html')
        res = template.render()
        return res

