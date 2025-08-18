{
    "name": "Custom Theme Color",
    "version": "1.0.2",
    "summary": "Custom navbar colors, icons, and left logo with click-to-home.",
    "category": "Theme/Backend",
    "depends": ["web"],
    "data": [],  # no XML files needed
    "assets": {
        "web.assets_backend": [
            "/custom_theme_color/static/src/css/custom_theme_color.css",
            "/custom_theme_color/static/src/js/logo_click.js",
        ],
    },
    "installable": True,
    "application": False,
}
