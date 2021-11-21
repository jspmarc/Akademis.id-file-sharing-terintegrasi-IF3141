# -*- coding: utf-8 -*-

from odoo import models, fields
from .._const import app_name


class Project(models.Model):
    _name = f'{app_name}.proyek'
    _description = 'File dan folder yang diletakkan di root.'
    _inherits = {
        f'{app_name}.file': 'file'
    }

    file = fields.Many2one(
        f'{app_name}.file', required=True, ondelete="cascade", delegate=True, auto_join=True)
