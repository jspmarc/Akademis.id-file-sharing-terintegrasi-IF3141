# -*- coding: utf-8 -*-

from odoo import models, fields


class Divisi(models.Model):
    _name = 'model.file_sharing.divisi'
    _description = 'Divisi yang dapat dimiliki User'

    name = fields.Char(string="Nama divisi", required=True)
    links = fields.One2many(
        'model.file_sharing.profile', 'id', string='Profile')
    projects = fields.One2many(
        'model.file_sharing.project', 'id', string='Projects')
