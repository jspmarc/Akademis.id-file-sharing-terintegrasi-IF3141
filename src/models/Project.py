# -*- coding: utf-8 -*-

from odoo import models, fields


class Project(models.Model):
    _name = 'filesharing.project'
    _description = 'Proyek yang mengandung file-file tertentu. Seperti folder.'

    name = fields.Char(string="Nama proyek", required=True)
