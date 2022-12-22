{
    'name': "Dog",
    'version': '16.0',
    'depends': ['base',],
    'author': "Sergio",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/dog_menus.xml',
        'views/dog_views.xml',
        'views/dog_points.xml',
    ],
}