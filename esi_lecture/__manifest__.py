# -*- coding: utf-8 -*-
{
    'name': "esi_lecture",

    'application': True,

    'summary':
        """Module that manages books.""",

    'description':
        """With this module we will be able to manage and sell books.""",

    'author': "Marika & Oscar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/res_partner_view.xml',
        'views/lecture_view.xml',
        'views/lecture_menu.xml',
        'views/product_template_view.xml',
        'demo/demo.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
