# -*- coding: utf-8 -*-

from odoo import models, fields
from .._const import app_name


class Divisi(models.Model):
    _name = f'{app_name}.jabatan'
    _description = 'Jabatan yang dapat dimiliki User'

    name = fields.Selection(
        selection=[
            ('admin', 'Admin'),
            ('bod', 'BoD'),
            ('staf', 'Staf')
        ],
        required=True,
        string="Nama jabatan",
        readonly=True,
    )
