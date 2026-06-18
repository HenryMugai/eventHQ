from flask import render_template

from flask_login import (
    login_required,
    current_user
)

from . import organiser_bp


@organiser_bp.route("/profile")
@login_required
def profile():

    return render_template(
        "organiser/profile.html",
        user=current_user
    )