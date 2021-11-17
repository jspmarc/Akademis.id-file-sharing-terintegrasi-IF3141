# -*- coding: utf-8 -*-
from odoo import http

app_name = 'file_sharing'
base_url = '/' + app_name


class Website(http.Controller):
    @http.route(f'{base_url}/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route(f'{base_url}/objects/', auth='public')
    def list(self, **kw):
        return http.request.render(f'{app_name}.listing', {
            'root': base_url,
            'objects': http.request.env[app_name].search([]),
        })

    @http.route(f'{base_url}/objects/<model("{base_url}"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render(f'{app_name}.object', {
            'object': obj
        })
