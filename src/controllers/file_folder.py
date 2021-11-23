# -*- coding: utf-8 -*-
from odoo import http
from .error import render_err
from .helpers import get_divisi_and_label, get_parent_to_root, remove_secrets, can_user_open
from .._const import app_name, base_url, complete_app_name


class File_Folder(http.Controller):
    @http.route(f'{base_url}file/<int:id>', auth='user', website=True)
    def file(self, id):
        env = http.request.env
        current_file = env[f'{app_name}.file'].browse([id])
        current_user = env[f'{app_name}.user'].search(
            [('user.id', '=', str(http.request.uid))]
        )

        if not current_file or current_file.type == 'folder':
            return render_err(http.request, 404, 'File not found.')

        if not can_user_open(current_file, current_user):
            return render_err(http.request, 401, 'Unauthorized.')

        return http.request.render(f'{complete_app_name}.show_file', {
            'data_file': current_file
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

        if not can_user_open(current_folder, current_user):
            return render_err(http.request, 401, 'Unauthorized.')

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
            'data_current_file': current_folder,
            'data_can_add_file': True,
            'data_can_see_secret': not cannot_see_secret,
        })

    @http.route(f'{base_url}file/add', auth='user')
    def add(self, **body):
        env = http.request.env

        tags_name = body['tags'].split(',')
        tags = []

        if 'is_secret' in body:
            tags_name.append('secret')
            body.pop('is_secret')

        for tag_name in tags_name:
            tag = env[f'{app_name}.file.tags'].search(
                [('name', '=', tag_name)])
            tags.append((4, tag.id))

        body['tags'] = tags

        env[f'{app_name}.file'].sudo().create(body)

        return http.Response(status=201)

    @http.route(f'{base_url}file/delete', auth='user')
    def delete(self, **body):
        env = http.request.env

        env[f'{app_name}.file'].browse([id]).unlink()

        return http.Response(status=200)

    @http.route(f'{base_url}file/edit', auth='user')
    def edit(self, **body):
        import logging

        logging.getLogger(__name__).info('--------------------------------')
        logging.getLogger(__name__).info(body)
        logging.getLogger(__name__).info('--------------------------------')

        return http.Response(status=200)
