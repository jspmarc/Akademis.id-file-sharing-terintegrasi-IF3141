# -*- coding: utf-8 -*-

from odoo import models, fields
from ._const import division_name
from .._const import app_name


class Divisi(models.Model):
    _name = f'{app_name}.divisi'
    _description = 'Divisi yang dapat dimiliki User'

    name = fields.Selection(string="Nama divisi",
                            required=True,
                            readonly=True,
                            selection=division_name)
    profil = fields.One2many(
        f'{app_name}.profil', 'divisi_owner', string='Profile')
    proyek = fields.One2many(
        f'{app_name}.proyek', 'divisi_owner', string='Proyek-proyek')
