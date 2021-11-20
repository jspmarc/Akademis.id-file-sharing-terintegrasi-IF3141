# -*- coding: utf-8 -*-

from odoo import models, fields
from .._const import app_name

divisionname = [
    ('product-mt-to', 'Master Teacher Try Out'),
    ('product-mt-vc', 'Master Teacher Virtual Class'),
    ('product-pm', 'Product Manager'),
    ('marketing-socmed', 'Social Media Strategist Team'),
    ('marketing-content', 'Marketing Content Production Team'),
    ('marketing-ambassador', 'Brand Ambassador Akademis.id'),
    ('creative-content', 'Creative Content Production'),
    ('creative-visual', 'Creative Visual Design'),
    ('creative-video', 'Video Editor'),
    ('creative-tiktok', 'Tiktok Talent'),
    ('creative-eo', 'Event Organizer'),
    ('creative-podcast', 'Podcast Talent'),
    ('finance-audit', 'Finance Audit'),
    ('finance-consumer', 'Consumer Research Team'),
    ('finance-business', 'Business Development Team'),
    ('it-fe', 'Frontend Developer Team'),
    ('it-be', 'Backend Developer Team'),
    ('it-apps', 'Apps Teams'),
    ('ceo-performance', 'People and Perforamce Team'),
    ('ceo-organizational', 'Organizational Development Team'),
]

etc = [
    ('secret', 'Rahasia Perusahaan')
]


class FileTags(models.Model):
    _name = f'{app_name}.file.tags'
    _description = 'Tag yang ada di sebuah file.'

    name = fields.Selection(string='Nama tag', required=True,
                            readonly=True, selection=divisionname + etc)
