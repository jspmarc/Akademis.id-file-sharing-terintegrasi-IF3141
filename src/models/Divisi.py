# -*- coding: utf-8 -*-

from odoo import models, fields


class Divisi(models.Model):
    _name = 'filesharing.divisi'
    _description = 'Divisi yang dapat dimiliki User'

    name = fields.Char(string="Nama divisi", required=True)
    links = fields.One2many(
        'filesharing.profil', 'id', string='Profile')
    projects = fields.One2many(
        'filesharing.project', 'id', string='Projects')
