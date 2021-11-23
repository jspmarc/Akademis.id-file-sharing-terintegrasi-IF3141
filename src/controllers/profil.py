# -*- coding: utf-8 -*-
from odoo import http
from .error import render_err
from .helpers import get_divisi_and_label, get_parent_to_root, remove_secrets, can_user_open, get_tags_from_list_of_names, get_profiles_divisi
from .._const import app_name, base_url, complete_app_name


class Profile(http.Controller):
    @http.route(f'{base_url}profil/add', auth='user')
    def add(self, **body):
        env = http.request.env

        divisi_owner = env[f'{app_name}.divisi'].search(
            [('name', '=', body['division_name'])]
        )
        body.pop('division_name')
        body['divisi_owner'] = divisi_owner.id

        env[f'{app_name}.profil'].sudo().create(body)

        return http.Response(status=201)