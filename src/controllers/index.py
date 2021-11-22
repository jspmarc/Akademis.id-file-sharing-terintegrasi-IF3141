# -*- coding: utf-8 -*-
from odoo import http
from .._const import app_name, base_url, complete_app_name


class Index(http.Controller):
    @http.route(f'{base_url}', auth='user', website=True)
    def index(self, **kw):
        env = http.request.env

        current_user = env[f'{app_name}.user'].search(
            [
                ('user.id', '=', str(http.request.uid))
            ]
        )
        if 'div' in kw:
            selected_division = kw['div']
        else:
            selected_division = current_user.divisi.name
        projects = env[f'{app_name}.proyek'].search(
            [('divisi_owner.name', '=?', selected_division)]
        )

        all_divisions_raw = env[f'{app_name}.divisi'].search([])
        all_divisions_name = []
        all_divisions_label = {}

        for divisi in all_divisions_raw:
            # Buat dapetin label
            label = dict(divisi._fields['name'].selection)[divisi.name]
            name = divisi.name

            all_divisions_label[name] = label
            all_divisions_name.append(name)

        return http.request.render(f'{complete_app_name}.index', {
            'data_shown_files': projects,
            'data_divisions_name': all_divisions_name,
            'data_divisions_label': all_divisions_label,
            'data_selected_division': selected_division,
            'data_path': '/',
        })
