import os

from flask import Blueprint, render_template

from .. import addones_dir_path
# from models import *

__all__ = ["mod"]

mod = Blueprint('blog', 'blog',
				  static_folder=os.path.join(addones_dir_path, 'statics'),
				  template_folder=os.path.join(addones_dir_path, 'templates'),
				  url_prefix='/')

@mod.route('blog/')
def index():
	return render_template('index.html')