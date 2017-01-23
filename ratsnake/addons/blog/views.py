from flask import Blueprint, render_template
# from models import *

__all__ = ["mod"]

mod = Blueprint('blog', 'blog',
				  static_folder="ratsnake/addons/blog/statics",
				  template_folder="ratsnake/addons/blog/templates",
				  url_prefix='/')

@mod.route('blog/')
def index():
	return render_template('index.html')