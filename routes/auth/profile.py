from flask import render_template

from flask_login import login_required
from flask_login import current_user

from . import auth_bp


@auth_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "auth/profile.html",
        user=current_user
    )