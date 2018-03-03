import json
import os
import psycopg2
import random
import string
import inspect

from flask import (request, render_template_string,
    redirect, current_app, abort, url_for)

from ...themes import get_current_theme, get_website_name, set_website_name
from ..web.models import Option, User
from ..web import database
from ..interface.flash import flash_error

from ratsnake.ext import db


SETUP_FOLDER_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
setup_template = open(os.path.join(SETUP_FOLDER_PATH, 'setup.html'), 'r').read().encode('utf8').decode('utf8')

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
            pg_host = request.form.get('pg_host')
            pg_user = request.form.get('pg_user')
            pg_pass = request.form.get('pg_pass')
            db_name = request.form.get('db_name')

            admin_username = request.form.get('admin_username')
            admin_password = request.form.get('admin_password')

            if not check_connection(pg_host, db_name, pg_user, pg_pass):
                message = "Cannot Connect to database!"
                return redirect(url_for('setup', message=message))

            with open('ratsnake/core/setup/config.template', 'r') as config_template_file:
                config_template = config_template_file.read()

            with open('config.json', 'w') as config_file:
                db_uri = generate_database_uri(pg_host, db_name, pg_user, pg_pass)
                new_temp = render_template_string(config_template,
                                        database_uri=db_uri,
                                        secret_key=request.form.get('secret_key'))
                current_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
                current_app.config['SECRET_KEY'] = request.form.get('secret_key')
                db.init_app(current_app)
                config_file.write(new_temp)
                
            database.create_all()
            set_website_name(request.form.get('website_name'))
            get_current_theme()

            user = User.query.filter_by(username=admin_username).first()
            if not user:
                user = User(
                    username=admin_username, password=admin_password, is_admin=True
                )
                user.set_admin()
                db.session.add(user)
            else:
                user.is_admin = True
                user.password = admin_password
            db.session.commit()


            return redirect('/')

        website_name = get_website_name() or "RatSnake"
        message = request.args.get('message')

        config = json.loads(open('config.json').read())
        sample_secret_key = ''.join(random.choice(
            string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(24))
        return render_template_string(setup_template,
                                    database_uri=config['SQLALCHEMY_DATABASE_URI'],
                                    website_name=website_name,
                                    message=message,
                                    secret_key=config['SECRET_KEY'],
                                    sample_secret_key=sample_secret_key)

def check_connection(host, database, user,
                     password, database_type="postgres"):
    connection_string_template = "dbname='{0}' user='{1}' password='{2}' host='{3}'"
    connection_string = connection_string_template.format(
        database, user, password, host
    )

    try:
        conn = psycopg2.connect(connection_string)
    except psycopg2.OperationalError as e:
        return False
    return True

def generate_database_uri(host, database, user, password,
                          database_type="postgres",
                          port=""):
    port = ":%s" % port if port else ""
    return "{database_type}://{user}:{password}@{host}{port}/{database}".format(
        database_type=database_type, user=user, password=password,
        database=database, host=host, port=port
    )

