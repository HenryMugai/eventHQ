from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import current_user

from services.auth_service import AuthService

from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:

        if current_user.role == "admin":
            return redirect(
                url_for("admin.dashboard")
            )

        if current_user.role == "organiser":
            return redirect(
                url_for("organiser.dashboard")
            )

    if request.method == "POST":

        email = request.form.get("email")

        password = request.form.get("password")

        user = AuthService.authenticate(
            email,
            password
        )

        if not user:

            flash(
                "Invalid email or password.",
                "danger"
            )

            return render_template(
                "auth/login.html"
            )

        AuthService.login(
            user
        )

        flash(
            "Login successful.",
            "success"
        )

        if user.role == "admin":

            return redirect(
                url_for(
                    "admin.dashboard"
                )
            )

        if user.role == "organiser":

            return redirect(
                url_for(
                    "organiser.dashboard"
                )
            )

        return redirect(
            url_for(
                "public.home"
            )
        )

    return render_template(
        "auth/login.html"
    )