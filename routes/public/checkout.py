from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from models.event import Event
from models.ticket_type import TicketType

from . import public_bp


@public_bp.route(
    "/checkout/<int:event_id>",
    methods=["GET", "POST"]
)
def checkout(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    ticket_types = TicketType.query.filter_by(
        event_id=event.id,
        is_active=True
    ).all()

    if request.method == "POST":

        flash(
            "Checkout flow will continue to payment module.",
            "info"
        )

        return redirect(
            url_for(
                "public.payment",
                event_id=event.id
            )
        )

    return render_template(
        "public/checkout.html",
        event=event,
        ticket_types=ticket_types
    )