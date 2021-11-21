# -*- coding: utf-8 -*-
from odoo import http
from .._const import app_name, base_url, complete_app_name


class Website(http.Controller):
    @http.route(f'{base_url}', auth='user', website=True)
    def index(self, **kw):
        Files = http.request.env[f'{app_name}.file']
        return http.request.render(f'{complete_app_name}.index', {
            'files': Files.search([])
        })
