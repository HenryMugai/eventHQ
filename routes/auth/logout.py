from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from services.auth_service import AuthService

from . import auth_bp


@auth_bp.route("/logout")
@login_required
def logout():

    AuthService.logout()

    flash(
        "Logged out successfully.",
        "success"
    )

    return redirect(
        url_for(
            "auth.login"
        )
    )