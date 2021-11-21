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
        'views/app-menu.xml',
        'views/app-trees.xml',
        'views/index.xml',
        'views/error/400.xml',

        'data/filesharing.file.csv',
        'data/filesharing.file.tags.csv',
        'data/filesharing.divisi.csv',

        'groups/jabatan.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['demo/demo.xml'],
    'qweb': [''],
    'installable': True,
    'application': True,
    'auto_install': False,
}
