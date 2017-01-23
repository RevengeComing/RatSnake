import os

def get_themes_list():
	theme_list = []
	for folder in os.walk('ratsnake/themes').next()[1]:
		if is_theme(folder):
			theme_list.append(folder)
	return theme_list

def is_theme(theme):
	theme_folder = 'ratsnake/themes/' + theme
	return True