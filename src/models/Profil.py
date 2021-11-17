# -*- coding: utf-8 -*-

from odoo import models, fields


class Profil(models.Model):
    _name = 'filesharing.profil'
    _description = 'Profil sebuah divisi'

    name = fields.Char(string='Nama link', required=True)
    link = fields.Char(required=True)
