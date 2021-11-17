# -*- coding: utf-8 -*-

from typing_extensions import Required
from odoo import models, fields


class Profil(models.Model):
    _name = 'model.file_sharing.profil'
    _description = 'Profil sebuah divisi'

    name = fields.Char(String='Nama link', required=True)
    link = fields.Char(Required=True)
