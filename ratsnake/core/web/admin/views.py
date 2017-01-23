from flask import Blueprint
from ..models import *

panel = Blueprint('panel', 'panel',
				  static_folder="ratsnake/core/panel/statics",
				  template_folder="ratsnake/core/panel/templates",
				  url_prefix='/rat_panel/')