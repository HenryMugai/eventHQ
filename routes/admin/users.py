from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from middleware import admin_required

from services.user_service import UserService

from . import admin_bp


@admin_bp.route("/users")
@admin_required
def users():

    users = UserService.get_all()

    return render_template(
        "admin/users/index.html",
        users=users
    )


@admin_bp.route(
    "/users/create",
    methods=["GET", "POST"]
)
@admin_required
def create_user():

    if request.method == "POST":

        UserService.create(
            full_name=request.form.get(
                "full_name"
            ),
            email=request.form.get(
                "email"
            ),
            phone=request.form.get(
                "phone"
            ),
            password=request.form.get(
                "password"
            ),
            role=request.form.get(
                "role"
            )
        )

        flash(
            "User created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "admin.users"
            )
        )

    return render_template(
        "admin/users/create.html"
    )


@admin_bp.route(
    "/users/<int:user_id>/suspend"
)
@admin_required
def suspend_user(user_id):

    user = UserService.get_by_id(
        user_id
    )

    if user:

        UserService.suspend(
            user
        )

        flash(
            "User suspended.",
            "success"
        )

    return redirect(
        url_for(
            "admin.users"
        )
    )


@admin_bp.route(
    "/users/<int:user_id>/activate"
)
@admin_required
def activate_user(user_id):

    user = UserService.get_by_id(
        user_id
    )

    if user:

        UserService.activate(
            user
        )

        flash(
            "User activated.",
            "success"
        )

    return redirect(
        url_for(
            "admin.users"
        )
    )


@admin_bp.route(
    "/users/<int:user_id>/reset-password",
    methods=["GET", "POST"]
)
@admin_required
def reset_password(user_id):

    user = UserService.get_by_id(
        user_id
    )

    if not user:

        flash(
            "User not found.",
            "danger"
        )

        return redirect(
            url_for(
                "admin.users"
            )
        )

    if request.method == "POST":

        UserService.reset_password(
            user,
            request.form.get(
                "password"
            )
        )

        flash(
            "Password reset successful.",
            "success"
        )

        return redirect(
            url_for(
                "admin.users"
            )
        )

    return render_template(
        "admin/users/reset_password.html",
        user=user
    )