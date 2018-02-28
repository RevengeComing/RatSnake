from flask import flash

__all__ = [
	'flash_success',
	'flash_info',
	'flash_warning',
	'flash_error'
]

def flash_success(message):
	flash(message, 'success')

def flash_info(message):
	flash(message, 'info')

def flash_warning(message):
	flash(message, 'warning')

def flash_error(message):
	flash(message, 'error')