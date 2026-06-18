from flask import send_file
from flask import flash
from flask import redirect
from flask import url_for

from flask_login import current_user

from middleware import organiser_required

from services.excel_service import (
    ExcelService
)

from models.event import Event
from models.ticket import Ticket

from . import organiser_bp


@organiser_bp.route(
    "/events/<int:event_id>/download-attendees"
)
@organiser_required
def download_attendees(event_id):

    organiser = current_user.organiser

    event = Event.query.filter_by(
        id=event_id,
        organiser_id=organiser.id
    ).first()

    if not event:

        flash(
            "Event not found.",
            "danger"
        )

        return redirect(
            url_for(
                "organiser.events"
            )
        )

    attendees = Ticket.query.filter_by(
        event_id=event.id
    ).all()

    filepath = (
        ExcelService.export_attendees(
            event,
            attendees
        )
    )

    return send_file(
        filepath,
        as_attachment=True
    )