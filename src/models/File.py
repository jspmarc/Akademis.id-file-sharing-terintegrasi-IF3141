# -*- coding: utf-8 -*-

from odoo import models, fields


class File(models.Model):
    _name = 'model.file_sharing.file'
    _description = 'File dan folder yang membentuk struktur data pada sistem.'

    parent_id = fields.parent_id(string='Parent ID', required=True, index=True)
    name = fields.char(String='Nama file', index=True, required=True)
    type = fields.Selection(
        selection=[('0', 'folder'), ('1', 'file')], required=True)
    tags = fields.One2many('model.file_sharing.file.tags',
                           'name', string='')


class FileTags(models.Model):
    _name = 'model.file_sharing.file.tags'
    _description = 'Tag yang ada di sebuah file.'

    name = fields.char(String='Nama tag', required=True)
