# -*- coding: utf-8 -*-

from odoo import models, fields


class Project(models.Model):
    _name = 'filesharing.project'
    _description = 'File dan folder yang diletakkan di root.'

    name = fields.Char(string="Nama proyek", required=True)
