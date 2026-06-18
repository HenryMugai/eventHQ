from flask import render_template

from models.ticket import Ticket

from . import public_bp


@public_bp.route(
    "/ticket/<string:ticket_number>"
)
def ticket_download(ticket_number):

    ticket = Ticket.query.filter_by(
        ticket_number=ticket_number
    ).first_or_404()

    return render_template(
        "public/ticket.html",
        ticket=ticket
    )