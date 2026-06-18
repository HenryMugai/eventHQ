from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import current_user

from middleware import admin_required

from services.event_service import (
    EventService
)

from models.category import Category
from models.organiser import Organiser

from . import admin_bp


@admin_bp.route("/events")
@admin_required
def events():

    events = EventService.get_all()

    return render_template(
        "admin/events/index.html",
        events=events
    )


@admin_bp.route(
    "/events/create",
    methods=["GET", "POST"]
)
@admin_required
def create_event():

    categories = Category.query.all()

    organisers = Organiser.query.all()

    if request.method == "POST":

        EventService.create(

            category_id=request.form.get(
                "category_id"
            ),

            organiser_id=request.form.get(
                "organiser_id"
            ),

            event_name=request.form.get(
                "event_name"
            ),

            short_description=request.form.get(
                "short_description"
            ),

            description=request.form.get(
                "description"
            ),

            venue=request.form.get(
                "venue"
            ),

            city=request.form.get(
                "city"
            ),

            start_datetime=request.form.get(
                "start_datetime"
            ),

            end_datetime=request.form.get(
                "end_datetime"
            ),

            created_by=current_user.id
        )

        flash(
            "Event created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "admin.events"
            )
        )

    return render_template(
        "admin/events/create.html",
        categories=categories,
        organisers=organisers
    )


@admin_bp.route(
    "/events/<int:event_id>/publish"
)
@admin_required
def publish_event(event_id):

    event = EventService.get_by_id(
        event_id
    )

    if event:

        EventService.publish(
            event
        )

    flash(
        "Event published.",
        "success"
    )

    return redirect(
        url_for(
            "admin.events"
        )
    )


@admin_bp.route(
    "/events/<int:event_id>/close"
)
@admin_required
def close_event(event_id):

    event = EventService.get_by_id(
        event_id
    )

    if event:

        EventService.close(
            event
        )

    flash(
        "Event closed.",
        "success"
    )

    return redirect(
        url_for(
            "admin.events"
        )
    )


@admin_bp.route(
    "/events/<int:event_id>/cancel"
)
@admin_required
def cancel_event(event_id):

    event = EventService.get_by_id(
        event_id
    )

    if event:

        EventService.cancel(
            event
        )

    flash(
        "Event cancelled.",
        "success"
    )

    return redirect(
        url_for(
            "admin.events"
        )
    )