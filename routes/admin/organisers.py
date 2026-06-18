from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from middleware import admin_required

from services.organiser_service import (
    OrganiserService
)

from . import admin_bp


@admin_bp.route("/organisers")
@admin_required
def organisers():

    organisers = (
        OrganiserService.get_all()
    )

    return render_template(
        "admin/organisers/index.html",
        organisers=organisers
    )


@admin_bp.route(
    "/organisers/create",
    methods=["GET", "POST"]
)
@admin_required
def create_organiser():

    if request.method == "POST":

        OrganiserService.create(
            company_name=request.form.get(
                "company_name"
            ),
            contact_person=request.form.get(
                "contact_person"
            ),
            email=request.form.get(
                "email"
            ),
            phone=request.form.get(
                "phone"
            ),
            password=request.form.get(
                "password"
            )
        )

        flash(
            "Organiser created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "admin.organisers"
            )
        )

    return render_template(
        "admin/organisers/create.html"
    )


@admin_bp.route(
    "/organisers/<int:organiser_id>/suspend"
)
@admin_required
def suspend_organiser(
    organiser_id
):

    organiser = (
        OrganiserService.get_by_id(
            organiser_id
        )
    )

    if organiser:

        OrganiserService.suspend(
            organiser
        )

    flash(
        "Organiser suspended.",
        "success"
    )

    return redirect(
        url_for(
            "admin.organisers"
        )
    )


@admin_bp.route(
    "/organisers/<int:organiser_id>/activate"
)
@admin_required
def activate_organiser(
    organiser_id
):

    organiser = (
        OrganiserService.get_by_id(
            organiser_id
        )
    )

    if organiser:

        OrganiserService.activate(
            organiser
        )

    flash(
        "Organiser activated.",
        "success"
    )

    return redirect(
        url_for(
            "admin.organisers"
        )
    )