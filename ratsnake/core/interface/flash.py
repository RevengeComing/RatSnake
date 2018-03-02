"""
Flashing functionalities for RatSnake.
"""

from flask import flash

__all__ = [
    'flash_success',
    'flash_info',
    'flash_warning',
    'flash_error'
]

def flash_success(message):
    """
    Flash a success message.

    Parameters:
    message: str
        the message you want to flash. 
    """
    flash(message, 'success')

def flash_info(message):
    """
    Flash a info message.

    Parameters:
    message: str
        the message you want to flash. 
    """
    flash(message, 'info')

def flash_warning(message):
    """
    Flash a warning message.

    Parameters:
    message: str
        the message you want to flash. 
    """
    flash(message, 'warning')

def flash_error(message):
    """
    Flash a error message.

    Parameters:
    message: str
        the message you want to flash. 
    """
    flash(message, 'error')