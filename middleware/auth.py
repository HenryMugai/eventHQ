from functools import wraps

from flask import flash
from flask import redirect
from flask import request
from flask import url_for

from flask_login import current_user


def login_required_custom(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if not current_user.is_authenticated:

            flash(
                "Please login to continue.",
                "warning"
            )

            return redirect(
                url_for(
                    "auth.login",
                    next=request.url
                )
            )

        return f(*args, **kwargs)

    return decorated_function