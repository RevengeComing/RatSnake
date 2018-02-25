import json
import os

from flask import request, render_template_string, redirect, current_app, abort

from ...themes import get_current_theme, get_website_name, set_website_name
from ..web.models import Option
from ..web import database
from ..interface.flash import flash_error

from ratsnake.ext import db

def setup(app):

    @app.before_request
    def check_config():
        if request.endpoint != "setup":
            if not current_app.config['SQLALCHEMY_DATABASE_URI']:
                return redirect('/setup_ratsnake/')

    @app.route('/setup_ratsnake/', methods=['GET', 'POST'])
    def setup():
        if current_app.config['SQLALCHEMY_DATABASE_URI']:
            abort(404)
        if request.method == "POST":
            if not validate_db_uri(request.form.get('database_uri')):
                flash_error("Database URI is Invalid!")
                return redirect('/setup_ratsnake/')
            with open('ratsnake/core/setup/config.template', 'r') as config_template_file:
                config_template = config_template_file.read()
            with open('config.json', 'w') as config_file:
                new_temp = render_template_string(config_template,
                                        database_uri=request.form.get('database_uri'),
                                        website_name=request.form.get('website_name'),
                                        secret_key=request.form.get('secret_key'),
                                        theme="default",
                                        active_addons="[]")
                config_file.write(new_temp)
                current_app.config['SQLALCHEMY_DATABASE_URI'] = request.form.get('database_uri')
                current_app.config['SECRET_KEY'] = request.form.get('secret_key')
                db.init_app(current_app)

                database.create_all()
                set_website_name(request.form.get('website_name'))
            return redirect('/')

        website_name = get_website_name() or "RatSnake"
        # theme = get_current_theme()

        config = json.loads(open('config.json').read())
        sample_secret_key = os.urandom(24)
        return render_template_string(open('ratsnake/core/setup/setup.html', 'r').read(),
                                        database_uri=config['SQLALCHEMY_DATABASE_URI'],
                                        website_name=website_name,
                                        # current_theme=theme,
                                        secret_key=config['SECRET_KEY'],
                                        sample_secret_key=sample_secret_key)

def validate_db_uri(user_input):
    res = user_input.split('://')
    db_type, res = res[0], res[1].split('/')
    if db_type != "mysql" and db_type != "postgres":
        flash_error("Database Type Not Supported")
        return False
    db_name, res = res[1], res[0].split('@')
    db_auth, db_addr = res[0].split(':'), res[1].split(':')
    print(db_addr)
    db_username, db_password = db_auth[0], db_auth[1]
    db_address = db_addr[0]
    if len(db_addr) > 1:
        db_port = db_addr[1]
        if db_port == "":
            flash_error("Dont Put ':' if not writing port.")
            return False
    else: db_port = ""
    if db_type and db_name and db_address and db_username and db_password and db_port == "":
        return True
    else:
        flash_error("Something Missing")
        return False   
