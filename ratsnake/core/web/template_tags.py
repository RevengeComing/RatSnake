from interface import menu_pages

def get_admin_menu():
	admin_menu = list()
	for menu_page in menu_pages:
		admin_menu.append({menu_page['menu_title']: menu_page['menu_title']['sub_menus']})
	return admin_menu

def get_menu():
	pass

def panel_tt_applier(app):
	app.jinja_env.globals['get_menus'] = get_menus

from ratsnake.core.interface import template_tags_appliers

template_tags_appliers.append(panel_tt_applier)