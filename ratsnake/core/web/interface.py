"""
This File Containing Interface Objects

menu_pages = [{'page_title':'Page Title',
               'menu_title': 'Menu Title',
               'url': '/some_path'
               'sub_menus':[{'route': '/route1',
                             'handler':some_function},
                            {'route': '/route2/<some_input>',
                             'handler': another_handler}] }, ... ]
"""

menu_pages = []

def add_menu_page(page_title, menu_title, sub_menus=[]):
    if not sub_menus is list:
        raise Exception("sub_menus object must be a list")
    if not page_title is str and not menu_title is str:
        raise Exception("page_title and menu_title object must be a string")
    page = {
        "page_title": page_title,
        "menu_title": menu_title,
        "sub_menus": sub_menus
    }
    menu_pages.append(page)

def add_sub_menu(menu_title, sub_menu):
    pass

def register_menu_pages():
    for menu_page in menu_pages:
        for key, value in menu_page['sub_menus']: