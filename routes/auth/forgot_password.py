from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for

from services.user_service import UserService

from . import auth_bp


@auth_bp.route(
    "/forgot-password",
    methods=["GET", "POST"]
)
def forgot_password():

    if request.method == "POST":

        email = request.form.get(
            "email"
        )

        user = UserService.get_by_email(
            email
        )

        if not user:

            flash(
                "Account not found.",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.forgot_password"
                )
            )

        flash(
            "Password reset functionality will be configured shortly.",
            "info"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "auth/forgot_password.html"
    )