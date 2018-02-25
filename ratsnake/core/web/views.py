from flask import Blueprint, render_template, current_app
from .models import *

web = Blueprint('web', 'web',
				  static_folder='ratsnake/themes/default/statics',
				  template_folder='ratsnake/themes/default/templates',
)

@web.route('/')
def index():
	return render_template('index.html')