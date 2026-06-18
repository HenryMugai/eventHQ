from flask import render_template

from models.event import Event

from . import public_bp


@public_bp.route(
    "/payment/<int:event_id>"
)
def payment(event_id):

    event = Event.query.get_or_404(
        event_id
    )

    return render_template(
        "public/payment.html",
        event=event
    )