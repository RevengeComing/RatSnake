from functools import wraps
from flask import abort

__all__ = [
    'permission_required',
    'staff_required',
    'admin_required'
]

def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def staff_required(view_handler):
    def wrapper():
        if current_user.is_authenticated:
            if current_user.is_staff:
                return view_handler
        abort(404)
        
    return wrapper

def admin_required(view_handler):
    def wrapper():
        if current_user.is_authenticated:
            if current_user.is_admin:
                return view_handler
        abort(404)
        
    return wrapper