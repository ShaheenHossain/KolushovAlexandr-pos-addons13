# -*- coding: utf-8 -*-
{
    'name': 'Available quantity of products in POS',
    'version': '10.0.1.1.0',
    'author': 'IT-Projects LLC, Ivan Yelizariev',
    'license': 'LGPL-3',
    'category': 'Point Of Sale',
    "support": "apps@it-projects.info",
    'website': 'https://twitter.com/yelizariev',
    'depends': ['point_of_sale', 'stock'],
    'data': [
        'data.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
}
