from flask import Flask, request, jsonify, redirect, url_for, render_template

from core import setup
from ext import  db, login_manager

__all__ = ['create_app']

DEFAULT_APP_NAME = 'ratsnake'

def create_app(app_name=DEFAULT_APP_NAME):

    app = Flask(app_name, static_folder='media/statics', template_folder='media/templates')

    configure_app(app)
    configure_theme(app)
    configure_addons(app)
    # configure_template_tag(app)
    configure_extentions(app)
    return app

def configure_app(app):
    import json
    config = json.loads(open('config.json', 'r').read())
    
    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    app.config['THEME'] = config['THEME']
    app.config['ACTIVE_ADDONS'] = config['THEME']
    app.config['SECRET_KEY'] = config['SECRET_KEY']

    setup.setup(app)

def configure_addons(app):
    from ratsnake.core.web.views import panel, web
    app.register_blueprint(panel)
    app.register_blueprint(web)

    from ratsnake import addons

    def get_subpackages(module):
        import os
        import glob
        dir = os.path.dirname(module.__file__)
        def is_package(d):
            d = os.path.join(dir, d)
            return os.path.isdir(d) and glob.glob(os.path.join(d, '__init__.py*'))

        return filter(is_package, os.listdir(dir))

    for subpackage in get_subpackages(addons):
        # print
        # try:
        addon = __import__('ratsnake.addons.%s' % subpackage, fromlist=['views'])
        app.register_blueprint(addon.views.mod)
        # except:
        #     print("%s is not an addon." % subpackage)

def configure_theme(app):
    app.template_folder = "ratsnake/themes/%s" % app.config["THEME"]
    app.static_folder = "ratsnake/themes/%s/statics" % app.config["THEME"]

def configure_errorhandlers(app):
    pass
    # @app.errorhandler(404)
    # def page_not_found(error):
    #     if request.is_xhr:
    #         return jsonify(error=_('Sorry, page not found')), 404

    #     return render_template("errors/404.html", error=error), 404

    # @app.errorhandler(403)
    # def forbidden(error):
    #     if request.is_xhr:
    #         return jsonify(error=_('Sorry, not allowed')), 403
    #     return render_template("errors/403.html", error=error), 403

    # @app.errorhandler(500)
    # def server_error(error):
    #     if request.is_xhr:
    #         return jsonify(error=_('Sorry, an error has occurred')), 500
    #     return render_template("errors/500.html", error=error), 500

    # @app.errorhandler(401)
    # def unauthorized(error):
    #     if request.is_xhr:
    #         return jsonify(error=_("Login required"))
    #     return redirect(url_for("profile.login", next=request.path))

def configure_template_tag(app):
    from ratsnake.core.interface import template_tags_appliers
    for applier in template_tags_appliers:
        template_tags_appliers(app)

def configure_extentions(app):
    db.init_app(app)
    login_manager.init_app(app)

