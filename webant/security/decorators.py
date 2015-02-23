from flask import redirect
from functools import wraps
from webant.security.capabilities import Capability
from webant.security.users import get_current_user


def _unauthorized():
    return redirect('/login')


def required_capabilities(*capabilities):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kw):
            caps = [Capability(capability) for capability in capabilities]
            user = get_current_user()
            if not user.can(caps):
                return _unauthorized()
        return decorated_view
    return wrapper
