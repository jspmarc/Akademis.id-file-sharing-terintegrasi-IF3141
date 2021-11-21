# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .._const import app_name, complete_app_name


class User(models.Model):
    _name = f'{app_name}.user'
    _description = 'User yang dapat mengakses sistem.'

    user = fields.Many2one(
        'res.users', required=True, ondelete="cascade")
    jabatan = fields.Many2one(f'{app_name}.jabatan', required=True, index=True)
    divisi = fields.Many2one(f'{app_name}.divisi', index=True)

    @api.model
    def create(self, vals):
        res = super(User, self).create(vals)
        if res['jabatan'] == 'admin':
            # kasih role administrator
            group_id = self.env.ref(f'{complete_app_name}.group_jabatan_admin')
        else:
            # kasih role karyawan
            group_id = self.env.ref(
                f'{complete_app_name}.group_jabatan_karyawan')
        group_id.users += res['user']
        return res
