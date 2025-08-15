{
    'name': 'Custom Theme Color',
    'version': '1.0',
    'category': 'Theme/Backend',
    'summary': 'Change backend colors such as navbar and buttons.',
    'author': 'Your Name',
    'depends': ['web'],
    'data': [
    ],
    "assets": {
        "web.assets_backend": [
            "/custom_theme_color/static/src/css/custom_theme_color.css",
        ],
    },
    'installable': True,
    'application': False,
}