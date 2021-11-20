# -*- coding: utf-8 -*-

from odoo import models, fields, api
from hashlib import pbkdf2_hmac
from secrets import token_hex, token_urlsafe
from .._const import app_name


class User(models.Model):
    _name = f'{app_name}.user'
    _description = 'User yang dapat mengakses sistem.'

    user_id = fields.Many2one('res.users', required=True)
    name = fields.Char(related='user_id.name', required=True)
    email = fields.Char(related='user_id.email',
                        store=True, index=True)
    password = fields.Char(
        default=lambda self: token_urlsafe(6), required=True)
    jabatan = fields.Many2one(f'{app_name}.jabatan', required=True, index=True)
    divisi = fields.Many2one(f'{app_name}.divisi', required=True, index=True)
    need_password_change = fields.Boolean(
        'Butuh perubahan password', default=True, required=True)

    @api.model  # It's either @api.model or @api.model_create_multi, gatau yang mana
    def create(self, vals):
        result = super(User, self).create(vals)

        # Ini pasti terlihat aneh, tapi percayalah ini harus dilakukan
        # untuk hashing password.
        # Secara internal, `result['password'] = ...` akan memanggil metode
        # `self.write` dan hashing password dilakukan pada metode tersebut.
        # Jika kode `result['password'] = ...` tidak ada, maka metode
        # `self.write` tidak akan dipanggil. Jika dilakukan
        # `result['password'] = self._secure_password(...)` jadi 2x hashing.
        # Yes, I hate Odoo too.
        result['password'] = result['password']

        return result

    def write(self, vals):
        vals['password'] = self._secure_password(vals['password'])
        res = super(User, self).write(vals)

        return res

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
