from flask import render_template
from flask import request

from services.checkin_service import (
    CheckinService
)

from . import public_bp


@public_bp.route(
    "/verify-ticket",
    methods=["GET", "POST"]
)
def verify_ticket():

    result = None

    if request.method == "POST":

        ticket_number = request.form.get(
            "ticket_number"
        )

        result = CheckinService.verify_ticket(
            ticket_number
        )

    return render_template(
        "public/verify_ticket.html",
        result=result
    )