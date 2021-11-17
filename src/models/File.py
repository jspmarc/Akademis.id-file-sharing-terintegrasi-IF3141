# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


class File(models.Model):
    _name = 'filesharing.file'
    _description = 'File dan folder yang membentuk struktur data pada sistem.'

    name = fields.Char(string='Nama file', index=True, required=True)
    link = fields.Char(string="Link ke file")
    type = fields.Selection(
        selection=[('0', 'folder'), ('1', 'file')], required=True)
    parent = fields.Many2one('filesharing.file',
                             index=True, default=0)
    tags = fields.Many2many('filesharing.file.tags', required=True)
    related_project = fields.Many2one(
        'filesharing.project', string='Related project', store=True)
