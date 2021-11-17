# -*- coding: utf-8 -*-

from odoo import models, fields
from hashlib import pbkdf2_hmac
from secrets import token_hex


class User(models.Model):
    _name = 'filesharing.user'
    _description = 'User yang dapat mengakses sistem.'

    user_id = fields.Many2one('res.users', required=True, invisible=True)
    name = fields.Char(related="user_id.partner_id.name",
                       required=True, store=True)
    email = fields.Char(related="user_id.partner_id.email",
                        required=True, store=True)
    password = fields.Char(related="user_id.password",
                           required=True)
    jabatan = fields.Many2one('filesharing.jabatan', required=True)
    divisi = fields.Many2one('filesharing.divisi', required=True)

    # def __generate_new_password(self):
    #     '''
    #     Fungsi untuk membuat sebuah password random baru
    #     '''
    #     rand = token_hex(6)
    #     salt = self.__generate_salt()
    #     password = rand + '$' + salt

    #     return (
    #         password,
    #         pbkdf2_hmac('sha256', bytearray(password, 'utf-8'),
    #                     bytearray(salt, 'utf-8'), 1000).hex()
    #     )

    # def __generate_salt(self, n: int = 12) -> str:
    #     return token_hex(n)

    # def __set_new_password(self):
    #     '''
    #     TODO
    #     '''
    #     pass
