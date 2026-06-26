from datetime import datetime

from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask_login import current_user
from flask_login import login_user

from database.db import bcrypt
from database.db import db

from models.user import User

from . import auth_bp


@auth_bp.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    if current_user.is_authenticated:

        if current_user.role.name == "admin":

            return redirect(
                url_for(
                    "admin.dashboard"
                )
            )

        return redirect(
            url_for(
                "organiser.dashboard"
            )
        )

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip().lower()

        password = request.form.get(
            "password",
            ""
        )

        remember = (
            request.form.get("remember")
            is not None
        )

        user = User.query.filter_by(
            email=email
        ).first()

        if user is None:

            flash(
                "Invalid email or password.",
                "danger"
            )

            return render_template(
                "auth/login.html"
            )

        if not bcrypt.check_password_hash(
            user.password_hash,
            password
        ):

            flash(
                "Invalid email or password.",
                "danger"
            )

            return render_template(
                "auth/login.html"
            )

        if not user.is_active:

            flash(
                "Your account has been suspended.",
                "warning"
            )

            return render_template(
                "auth/login.html"
            )

        user.last_login = datetime.utcnow()

        db.session.commit()

        login_user(
            user,
            remember=remember
        )

        flash(
            f"Welcome back, {user.first_name}.",
            "success"
        )

        role = user.role.name.lower()

        if role == "admin":

            return redirect(
                url_for(
                    "admin.dashboard"
                )
            )

        if role == "organiser":

            return redirect(
                url_for(
                    "organiser.dashboard"
                )
            )

        flash(
            "Your account role is not configured.",
            "danger"
        )

        return redirect(
            url_for(
                "auth.logout"
            )
        )

    return render_template(
        "auth/login.html"
    )