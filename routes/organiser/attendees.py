from flask import render_template

from flask_login import current_user

from middleware import organiser_required

from models.ticket import Ticket
from models.event import Event

from . import organiser_bp


@organiser_bp.route(
    "/events/<int:event_id>/attendees"
)
@organiser_required
def attendees(event_id):

    organiser = current_user.organiser

    event = Event.query.filter_by(
        id=event_id,
        organiser_id=organiser.id
    ).first_or_404()

    attendees = Ticket.query.filter_by(
        event_id=event.id
    ).all()

    return render_template(
        "organiser/attendees/index.html",
        event=event,
        attendees=attendees
    )