import os
import inspect
import json

from ratsnake import flash_warning
from ratsnake.core.web.models import Option

addones_dir_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

def get_active_addones():
    active_addones = Option.query.filter_by(name="active_addones").first()
    return json.loads(active_addones.value)

def add_addone(addone):
    active_addones = get_active_addones()
    if addone in active_addones:
        # TODO: Convert to flash message
        flash_warning('addone is already activated')
        return

    # TODO: call database upgrade
    # TODO: add addone to active_addones and commit