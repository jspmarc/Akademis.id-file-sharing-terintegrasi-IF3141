# -*- coding: utf-8 -*-
from odoo import http
from .._const import app_name, base_url, complete_app_name


class Fndex(http.Controller):
    @http.route(f'{base_url}file/<int:id>', auth='user', website=True)
    def file(self, **kw):
        env = http.request.env

    @http.route(f'{base_url}folder/<int:id>', auth='user', website=True)
    def file(self, **kw):
        env = http.request.env
