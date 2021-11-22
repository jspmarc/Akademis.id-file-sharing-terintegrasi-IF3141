# -*- coding: utf-8 -*-
from odoo import http
from .._const import app_name, base_url, complete_app_name


class File_Folder(http.Controller):
    @http.route(f'{base_url}file/<int:id>', auth='user', website=True)
    def file(self, id):
        env = http.request.env
        cur_file = env[f'{app_name}.file'].browse([id])

        print(cur_file['name'], cur_file['name'],
              cur_file['parent'], cur_file['tags'])

        return http.request.render(f'{complete_app_name}.show_file', {
            'data_file': cur_file
        })

    @http.route(f'{base_url}folder/<int:id>', auth='user', website=True)
    def folder(self, id):
        env = http.request.env
        cur_file = env[f'{app_name}.file'].browse([id])

        print(cur_file['name'], cur_file['name'],
              cur_file['parent'], cur_file['tags'])

        return http.request.render(f'{complete_app_name}.show_file', {
            'data_file': cur_file
        })
