# -*- coding: utf-8 -*-
# TODO: Isi
{
    'name': 'File Sharing Terintegrasi',
    'summary': '',
    'description': '',
    'sequence': -100,
    'author': '',
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base', 'website'],
    'data': [
        'groups/jabatan.xml',

        'views/app-menu.xml',
        'views/app-trees.xml',

        'views/file-section.xml',
        'views/file-header-section.xml',
        'views/index.xml',
        'views/error.xml',

        'data/filesharing.divisi.csv',
        'data/filesharing.file.csv',
        'data/filesharing.file.tags.csv',
        'data/filesharing.jabatan.csv',

        'security/ir.model.access.csv',
    ],
    'demo': ['demo/demo.xml'],
    'qweb': [''],
    'installable': True,
    'application': True,
    'auto_install': False,
}
