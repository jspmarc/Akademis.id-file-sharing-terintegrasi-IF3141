# -*- coding: utf-8 -*-

from odoo import models, fields, api
from hashlib import pbkdf2_hmac
from secrets import token_hex, token_urlsafe


class User(models.Model):
    _name = 'filesharing.user'
    _description = 'User yang dapat mengakses sistem.'

    user_id = fields.Many2one('res.users', required=True)
    name = fields.Char(related='user_id.name', required=True)
    email = fields.Char(related='user_id.email',
                        store=True, index=True)
    password = fields.Char(
        default=lambda self: token_urlsafe(6), required=True)
    jabatan = fields.Many2one('filesharing.jabatan', required=True, index=True)
    divisi = fields.Many2one('filesharing.divisi', required=True, index=True)
    need_password_change = fields.Boolean(
        'Butuh perubahan password', default=True, required=True)

    @api.model_create_multi
    def create(self, vals):
        result = super(User, self).create(vals)
        result['password'] = self._secure_password(result['password'])

        return result

    def _secure_password(self, unsecure_password):
        '''
        Fungsi untuk membuat sebuah password random baru
        '''
        salt = self._generate_salt()
        password = salt + unsecure_password + salt

        return pbkdf2_hmac('sha512', bytearray(password, 'utf-8'),
                           bytearray(salt, 'utf-8'), 1000).hex() + '$' + salt

    def _generate_salt(self, n: int = 12) -> str:
        return token_hex(n)
