import json

import sqlalchemy
from flask import Flask, request, jsonify, redirect, url_for, render_template

from .themes import get_current_theme
from .core import setup
from .core.web.models import Option
from .ext import  db, login_manager

__all__ = ['create_app']

DEFAULT_APP_NAME = 'ratsnake'


class RatSnake(Flask):
    def teardown_appcontext(self, f):
        self.teardown_appcontext_funcs.append(f)
        return f


def create_app(app_name=DEFAULT_APP_NAME):

    app = RatSnake(app_name)

    configure_app(app)
    configure_extentions(app)
    configure_theme(app)
    configure_addons(app)
    # configure_template_tag(app)
    return app

def configure_app(app):    
    config = json.loads(open('config.json', 'r').read())
    
    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config['SECRET_KEY'] = config['SECRET_KEY']

    setup.setup(app)

def configure_addons(app):
    from ratsnake.core.web.views import web
    from ratsnake.core.panel.views import panel
    app.register_blueprint(panel)
    app.register_blueprint(web)

    from ratsnake import addons

    def get_subpackages(module):
        import os
        import glob
        directory = os.path.dirname(module.__file__)
        def is_package(d):
            d = os.path.join(directory, d)
            return os.path.isdir(d) and glob.glob(os.path.join(d, '__init__.py*'))

        return filter(is_package, os.listdir(directory))

    for subpackage in get_subpackages(addons):
        addon = __import__('ratsnake.addons.%s' % subpackage, fromlist=['views'])
        app.register_blueprint(addon.views.mod)

def configure_theme(app):
    with app.app_context():
        theme = get_current_theme()
        if theme:
            app.template_folder = "themes/%s/templates" % theme.value
            app.static_folder = "themes/%s/statics" % theme.value


def configure_errorhandlers(app):
    pass

def configure_template_tag(app):
    from ratsnake.core.interface import template_tags_appliers
    for applier in template_tags_appliers:
        template_tags_appliers(app)

def configure_extentions(app):
    db.init_app(app)
    login_manager.init_app(app)