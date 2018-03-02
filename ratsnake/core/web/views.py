from flask import Blueprint, render_template, current_app
from .models import *

web = Blueprint('web', 'web')

@web.route('/')
def index():
    return render_template('index.html')