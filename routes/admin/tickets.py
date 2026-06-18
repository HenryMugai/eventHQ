from flask import render_template

from middleware import admin_required

from models.ticket import Ticket

from . import admin_bp


@admin_bp.route("/tickets")
@admin_required
def tickets():

    tickets = Ticket.query.order_by(
        Ticket.issued_at.desc()
    ).all()

    return render_template(
        "admin/tickets/index.html",
        tickets=tickets
    )