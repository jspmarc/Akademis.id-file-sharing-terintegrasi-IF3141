# -*- coding: utf-8 -*-

from odoo import models, fields


class Project(models.Model):
    _name = 'model.file_sharing.project'
    _description = 'Proyek yang mengandung file-file tertentu. Seperti folder.'

    name = fields.Char(String="Nama proyek", required=True)
