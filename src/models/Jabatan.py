# -*- coding: utf-8 -*-

from odoo import models, fields


class Divisi(models.Model):
    _name = 'filesharing.jabatan'
    _description = 'Jabatan yang dapat dimiliki User'

    name = fields.Selection(
        selection=[
            ('0', 'admin'),
            ('1', 'BoD'),
            ('2', 'staf')
        ],
        required=True,
        string="Nama jabatan"
    )
