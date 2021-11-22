# -*- coding: utf-8 -*-

from odoo import models, fields
from .._const import app_name


class Profil(models.Model):
    _name = f'{app_name}.profil'
    _description = 'Profil sebuah divisi'

    name = fields.Char(string='Nama link', required=True)
    link = fields.Char(required=True)
    divisi_owner = fields.Many2one(
        f'{app_name}.divisi', index=True, required=True)
