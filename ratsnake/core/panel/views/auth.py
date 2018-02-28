from flask import render_template, redirect, url_for

from flask_login import login_user

from ratsnake import flash_error

from . import panel
from ...web.models import *

from ..forms import LoginForm

@panel.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user, remember_me)
            return redirect(url_for('panel.dashboard'))
        flash_error('Invalid username or password.')
    return render_template('login.html', form=form)

@panel.route('/logout/')
def logout():
    pass