from ratsnake import staff_required, admin_required

from flask import Blueprint, redirect, url_for, render_template, current_app

from flask_login import current_user

panel = Blueprint(
	'panel', 'panel',
    static_folder="ratsnake/core/panel/front/dist/static",
    template_folder="ratsnake/core/panel/front",
    url_prefix='/rs-admin'
)

from . import auth
from . import api

@panel.after_request
def add_cors(resp):
    if current_app.debug:
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    return resp

@panel.route('/')
def index():
	if current_user.is_authenticated:
		return redirect(url_for('panel.dashboard'))
	return redirect(url_for('panel.login'))


@staff_required
@panel.route('/dashboard/')
def dashboard():
	return render_template('dist/dashboard.html')