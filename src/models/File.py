# -*- coding: utf-8 -*-

from odoo import models, fields


class File(models.Model):
    _name = 'model.file_sharing.file'
    _description = 'File dan folder yang membentuk struktur data pada sistem.'

    name = fields.Char(String='Nama file', index=True, required=True)
    link = fields.Char(String="Link ke file", required=True)
    type = fields.Selection(
        selection=[('0', 'folder'), ('1', 'file')], required=True)
    parent = fields.Many2one('model.file_sharing.file',
                             required=True, index=True)
    tags = fields.One2many('model.file_sharing.file.tags',
                           'name', string='')


class FileTags(models.Model):
    _name = 'model.file_sharing.file.tags'
    _description = 'Tag yang ada di sebuah file.'

    name = fields.Char(String='Nama tag', required=True)
