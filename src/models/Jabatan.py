# -*- coding: utf-8 -*-

from odoo import models, fields


class Divisi(models.Model):
    _name = 'filesharing.jabatan'
    _description = 'Jabatan yang dapat dimiliki User'

    name = fields.Selection(
        selection=[
            ('admin', 'Admin'),
            ('bod', 'BoD'),
            ('staf', 'Staf')
        ],
        required=True,
        string="Nama jabatan"
    )
