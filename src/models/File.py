# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .._const import app_name


class File(models.Model):
    _name = f'{app_name}.file'
    _description = 'File dan folder yang membentuk struktur data pada sistem.'

    name = fields.Char(string='Nama file', index=True, required=True)
    link = fields.Char(string="Link ke file")
    type = fields.Selection(
        selection=[('0', 'folder'), ('1', 'file')], required=True)
    parent = fields.Many2one(f'{app_name}.file',
                             index=True, default=0)
    tags = fields.Many2many(f'{app_name}.file.tags', required=True)
