# -*- coding: utf-8 -*-

from odoo import models, fields


class Divisi(models.Model):
    _name = 'model.akademisid.divisi'
    _description = 'Divisi yang dapat dimiliki User'

    name = fields.Char(string="Nama divisi", required=True)
