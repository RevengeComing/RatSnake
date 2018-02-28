from flask import Blueprint, redirect, url_for, render_template

from flask_login import current_user

panel = Blueprint(
	'panel', 'panel',
    static_folder="ratsnake/core/panel/front/dist/static",
    template_folder="ratsnake/core/panel/front/dist",
    url_prefix='/rs-admin'
)

from . import auth

@panel.route('/')
def index():
	if current_user.is_authenticated:
		return redirect(url_for('panel.dashboard'))
	return redirect(url_for('panel.login'))

@panel.route('/dashboard/')
def dashboard():
	return render_template('dashboard.html')
