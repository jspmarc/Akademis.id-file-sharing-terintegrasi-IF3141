# -*- coding: utf-8 -*-
from odoo import http
from .._const import app_name, base_url, complete_app_name
import logging


class Index(http.Controller):
    __logger = logging.getLogger(__name__)

    @http.route(f'{base_url}', auth='user', website=True)
    def index(self, **kw):
        env = http.request.env

        files = env[f'{app_name}.file'].search([])
        projects = env[f'{app_name}.proyek'].search([])

        return http.request.render(f'{complete_app_name}.index', {
            'shown_files': files
        })
