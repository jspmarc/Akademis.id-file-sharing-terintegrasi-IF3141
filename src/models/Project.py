# -*- coding: utf-8 -*-

from odoo import models, fields
from .._const import app_name


class Project(models.Model):
    _name = f'{app_name}.project'
    _description = 'File dan folder yang diletakkan di root.'

    name = fields.Char(string="Nama proyek", required=True)
