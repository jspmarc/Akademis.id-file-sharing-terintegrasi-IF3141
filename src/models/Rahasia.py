# -*- coding: utf-8 -*-

from odoo import models, fields, api
from .._const import app_name


class Secret(models.Model):
    _name = f'{app_name}.rahasia'
    _description = 'File dan folder rahasia pada sistem.'
    _inherits = {
        f'{app_name}.file': 'file'
    }

    file = fields.Many2one(
        f'{app_name}.file', required=True, ondelete="cascade", delegate=True, auto_join=True)
