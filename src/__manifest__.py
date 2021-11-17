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
    'depends': ['base'],
    'data': [
        'views/app-menu.xml',
        'views/user-tree.xml',
        'views/templates.xml',
        'data/filesharing.file.tags.csv',
        'data/filesharing.jabatan.csv',
        'data/filesharing.divisi.csv',
        'security/ir.model.access.csv',
    ],
    'demo': ['demo/demo.xml'],
    'qweb': [''],
    'installable': True,
    'application': True,
    'auto_install': False,
}
