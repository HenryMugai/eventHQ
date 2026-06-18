from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from middleware import admin_required

from database.db import db

from models.event import Event
from models.ticket_type import TicketType

from . import admin_bp


@admin_bp.route("/ticket-types")
@admin_required
def ticket_types():

    ticket_types = TicketType.query.all()

    return render_template(
        "admin/ticket_types/index.html",
        ticket_types=ticket_types
    )


@admin_bp.route(
    "/events/<int:event_id>/ticket-types/create",
    methods=["GET", "POST"]
)
@admin_required
def create_ticket_type(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    if request.method == "POST":

        ticket_type = TicketType(
            event_id=event.id,
            name=request.form.get("name"),
            description=request.form.get("description"),
            price=request.form.get("price"),
            quantity=request.form.get("quantity"),
            max_per_order=request.form.get("max_per_order")
        )

        db.session.add(ticket_type)

        db.session.commit()

        flash(
            "Ticket type created successfully.",
            "success"
        )

        return redirect(
            url_for(
                "admin.ticket_types"
            )
        )

    return render_template(
        "admin/ticket_types/create.html",
        event=event
    )