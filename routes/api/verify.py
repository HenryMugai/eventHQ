from flask import jsonify

from services.checkin_service import (
    CheckinService
)

from . import api_bp


@api_bp.route(
    "/verify/<string:ticket_number>"
)
def verify_ticket(ticket_number):

    result = CheckinService.verify_ticket(
        ticket_number
    )

    if not result["success"]:

        return jsonify(result), 404

    ticket = result["ticket"]

    return jsonify({

        "success": True,

        "ticket_number": ticket.ticket_number,

        "attendee_name": ticket.attendee_name,

        "attendee_email": ticket.attendee_email,

        "attendee_phone": ticket.attendee_phone,

        "status": ticket.status
    })