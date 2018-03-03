from functools import wraps
from collections import OrderedDict

from flask import jsonify

__all__ = [
    'sidebar_links',
    'add_sidebar_link',
    'sidebar_link',
]


class SidebarLinks(object):
    instance = None

    class __SidbarLinks(object):
        def __init__(self):
            self.links = OrderedDict()

    def __init__(self):
        if not SidebarLinks.instance:
            SidebarLinks.instance = SidebarLinks.__SidbarLinks()
        else:
            raise Exception("You can't create multiple SidebarLinks object.")

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def add_link(self, view_handler, title, parent):
        link = {'handler': view_handler, 'childs':OrderedDict()}
        if parent:
            SidebarLinks.instance.links[parent]['childs'][title] = link
        else:
            SidebarLinks.instance.links[title] = link

    def jsonify(self):
        return jsonify(SidebarLinks.instance.links) 


sidebar_links = SidebarLinks()


def add_sidebar_link(view_handler, title, parent):
    global sidebar_links
    sidebar_links.add_link(view_handler, title, parent)


def sidebar_link(title, parent=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            add_sidebar_link(f, title, parent)
            return f(*args, **kwargs)
        return decorated_function()
    return decorator