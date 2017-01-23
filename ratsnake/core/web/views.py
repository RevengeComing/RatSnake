from flask import Blueprint, render_template, current_app
from models import *
from admin.views import panel

web = Blueprint('web', 'web',
				  # static_folder="ratsnake/core/web/statics",
				  # template_folder="ratsnake/core/web/templates",
				  url_prefix='/')

@web.route('')
def index():
	print current_app.template_folder
	return render_template('index.html')