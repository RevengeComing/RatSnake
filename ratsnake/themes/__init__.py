import sqlalchemy

from flask import current_app

from ratsnake.core.web.models import Option
from ratsnake.ext import db

def set_theme(theme_name):
    current_app.template_folder = 'themes/%s/templates' % theme_name
    current_app.static_folder = "themes/%s/statics" % theme_name

def get_current_theme():
    try:
        theme = Option.query.filter_by(name='theme').first()
        if not theme:
            set_current_theme('default')
        return theme
    except sqlalchemy.exc.ArgumentError:
        print(' * RatSnake is not installed yet.')

def set_current_theme(theme_name):
    theme = Option.query.filter_by(name="theme").first()
    if theme:
        theme.value = theme_name
    else:
        theme = Option(name="theme", value=theme_name)
        db.session.add(theme)
    set_theme(theme.value)
    db.session.commit()

def get_website_name():
    try:
        website_name = Option.query.filter_by(name="website_name").first()
        if not website_name:
            website_name = Option(name='website_name', value='RatSnake')
            db.session.add(website_name)
            db.session.commit()
        return website_name
    except sqlalchemy.exc.ArgumentError:
        print(' * RatSnake is not installed yet.')

def set_website_name(name):
    website_name = Option.query.filter_by(name="website_name").first()
    if website_name:
        website_name.value = name
    else:
        website_name = Option(name="website_name", value=name)
        db.session.add(website_name)
    db.session.commit()