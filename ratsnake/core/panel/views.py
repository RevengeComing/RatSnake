from flask import Blueprint, render_template

from ..web.models import *

from .forms import LoginForm

panel = Blueprint('panel', 'panel',
                static_folder="ratsnake/core/panel/statics",
                template_folder="ratsnake/core/panel/templates",
                url_prefix='/rs-admin'
            )

@panel.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        
    return render_template('login.html', form=form)

@panel.route('/logout/')
def logout():
    pass