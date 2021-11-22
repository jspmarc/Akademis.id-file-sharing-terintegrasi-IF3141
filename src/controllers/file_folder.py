# -*- coding: utf-8 -*-
from odoo import http
from .error import render_err
from .helpers import get_divisi_and_label, get_parent_to_root, remove_secrets
from .._const import app_name, base_url, complete_app_name


class File_Folder(http.Controller):
    # TODO: Ngecek user-nya punya hak buat buak folder/file tertentu atau tidak

    @http.route(f'{base_url}file/<int:id>', auth='user', website=True)
    def file(self, id):
        env = http.request.env
        cur_file = env[f'{app_name}.file'].browse([id])

        if not cur_file or cur_file.type == 'folder':
            return render_err(http.request, 404, 'File not found.')

        return http.request.render(f'{complete_app_name}.show_file', {
            'data_file': cur_file
        })

    @http.route(f'{base_url}folder/<int:id>', auth='user', website=True)
    def folder(self, id):
        if id == 1:
            return http.request.redirect('/')

        env = http.request.env

        current_user = env[f'{app_name}.user'].search(
            [('user.id', '=', str(http.request.uid))]
        )
        current_folder = env[f'{app_name}.file'].browse([id])
        cannot_see_secret = current_user.jabatan.name == 'staf'

        if not current_folder or current_folder.type == 'file':
            return render_err(http.request, 404, 'Folder not found.')

        files = env[f'{app_name}.file'].search([
            ('parent.id', '=', str(id)),
            ('tags.name', '=?', current_user.divisi.name if current_user.jabatan.name !=
             'admin' else False),
        ])

        # FIXME: ini cursed but im too tired
        if cannot_see_secret:
            files = filter(remove_secrets, files)

        (all_divisions_name, all_divisions_label) = get_divisi_and_label(env)
        path = get_parent_to_root(env, id)

        return http.request.render(f'{complete_app_name}.index', {
            'data_shown_files': files,
            'data_divisions_name': all_divisions_name,
            'data_divisions_label': all_divisions_label,
            'data_selected_division': current_folder,
            'data_path': path,
        })
