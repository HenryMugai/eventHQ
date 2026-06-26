from functools import wraps

from flask import abort

from flask_login import current_user


def organiser_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if not current_user.is_authenticated:

            abort(401)

        if not current_user.is_active:

            abort(403)

        if current_user.role is None:

            abort(403)

        if current_user.role.name != "organiser":

            abort(403)

        return f(*args, **kwargs)

    return decorated_function