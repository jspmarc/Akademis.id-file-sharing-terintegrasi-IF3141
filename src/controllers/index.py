# -*- coding: utf-8 -*-
from odoo import http
from .helpers import get_divisi_and_label, remove_secrets
from .._const import app_name, base_url, complete_app_name


class Index(http.Controller):
    @http.route(f'{base_url}', auth='user', website=True)
    def index(self, **kw):
        env = http.request.env

        current_user = env[f'{app_name}.user'].search(
            [('user.id', '=', str(http.request.uid))]
        )
        if 'div' in kw:
            selected_division = kw['div']
        else:
            selected_division = current_user.divisi.name

        can_see_secret = current_user.jabatan.name != 'staf'

        projects = env[f'{app_name}.proyek'].search([
            ('divisi_owner.name', '=?', selected_division),
            ('tags.name', '=?', current_user.divisi.name if current_user.jabatan.name !=
             'admin' else False),
            # ('file.tags.name', '!=', 'secret'),
        ])

        # FIXME: ini cursed but im too tired
        if not can_see_secret:
            projects = filter(remove_secrets, projects)

        (all_divisions_name, all_divisions_label) = get_divisi_and_label(env)

        return http.request.render(f'{complete_app_name}.index', {
            'data_shown_files': projects,
            'data_divisions_name': all_divisions_name,
            'data_divisions_label': all_divisions_label,
            'data_selected_division': selected_division,
            'data_path': [{'link': '/', 'label': 'root'}],
            'data_current_file': env[f'{app_name}.file'].browse([1]),
            'data_can_add_file': False,
            'data_can_see_secret': can_see_secret,
        })
