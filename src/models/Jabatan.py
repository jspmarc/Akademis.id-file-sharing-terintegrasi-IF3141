# -*- coding: utf-8 -*-

from odoo import models, fields


class Divisi(models.Model):
    _name = 'model.file_sharing.jabatan'
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
