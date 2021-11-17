# -*- coding: utf-8 -*-

from odoo import models, fields
from . import FileTags


class Divisi(models.Model):
    _name = 'filesharing.divisi'
    _description = 'Divisi yang dapat dimiliki User'

    name = fields.Selection(string="Nama divisi",
                            required=True,
                            store=True,
                            selection=FileTags.FileTags.divisionname)
    profil = fields.One2many(
        'filesharing.profil', 'id', string='Profile')
    projects = fields.One2many(
        'filesharing.project', 'id', string='Projects')
