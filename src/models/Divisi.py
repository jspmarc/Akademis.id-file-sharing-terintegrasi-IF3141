# -*- coding: utf-8 -*-

from odoo import models, fields
from . import FileTags
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
        f'{app_name}.profil', 'id', string='Profile')
    projects = fields.One2many(
        f'{app_name}.project', 'id', string='Projects')
