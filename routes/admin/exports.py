from flask import send_file

from middleware import admin_required

from models.event import Event
from models.ticket import Ticket

from services.excel_service import (
    ExcelService
)

from . import admin_bp


@admin_bp.route(
    "/exports/attendees/<int:event_id>"
)
@admin_required
def export_attendees(event_id):

    event = Event.query.get_or_404(
        event_id
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