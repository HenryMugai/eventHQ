from datetime import datetime
from uuid import uuid4

from database.db import db

from models.ticket import Ticket
from models.ticket_type import TicketType


class TicketService:

    @staticmethod
    def generate_ticket_number():

        year = datetime.now().year

        unique = str(uuid4()).replace("-", "")[:8].upper()

        return f"EVHQ-{year}-{unique}"

    @staticmethod
    def create_ticket(
        event_id,
        ticket_type_id,
        attendee_name,
        attendee_email,
        attendee_phone,
        order_id=None,
        ticket_source="online"
    ):

        ticket = Ticket(
            order_id=order_id,
            event_id=event_id,
            ticket_type_id=ticket_type_id,
            ticket_number=TicketService.generate_ticket_number(),
            attendee_name=attendee_name,
            attendee_email=attendee_email,
            attendee_phone=attendee_phone,
            ticket_source=ticket_source,
            status="valid"
        )

        db.session.add(ticket)

        ticket_type = TicketType.query.get(ticket_type_id)

        if ticket_type:
            ticket_type.sold += 1

        db.session.commit()

        return ticket

    @staticmethod
    def get_by_id(ticket_id):

        return Ticket.query.get(ticket_id)

    @staticmethod
    def get_by_ticket_number(ticket_number):

        return Ticket.query.filter_by(
            ticket_number=ticket_number
        ).first()

    @staticmethod
    def get_event_tickets(event_id):

        return Ticket.query.filter_by(
            event_id=event_id
        ).all()

    @staticmethod
    def cancel(ticket):

        ticket.status = "cancelled"

        db.session.commit()

    @staticmethod
    def refund(ticket):

        ticket.status = "refunded"

        db.session.commit()

    @staticmethod
    def mark_used(ticket):

        ticket.status = "used"

        db.session.commit()

    @staticmethod
    def delete(ticket):

        db.session.delete(ticket)

        db.session.commit()