# -*- coding: utf-8 -*-

from odoo import models, fields
from .._const import app_name
from ._const import division_name, etc


class FileTags(models.Model):
    _name = f'{app_name}.file.tags'
    _description = 'Tag yang ada di sebuah file.'

    name = fields.Selection(string='Nama tag', required=True,
                            readonly=True, selection=division_name + etc)
