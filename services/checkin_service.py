from datetime import datetime

from database.db import db

from models.ticket import Ticket
from models.checkin import CheckIn


class CheckinService:

    @staticmethod
    def verify_ticket(ticket_number):

        ticket = Ticket.query.filter_by(
            ticket_number=ticket_number
        ).first()

        if not ticket:

            return {
                "success": False,
                "message": "Invalid Ticket"
            }

        if ticket.status == "used":

            return {
                "success": False,
                "message": "Ticket Already Used"
            }

        if ticket.status != "valid":

            return {
                "success": False,
                "message": "Ticket Not Valid"
            }

        return {
            "success": True,
            "ticket": ticket
        }

    @staticmethod
    def check_in(ticket, user_id=None):

        ticket.status = "used"

        log = CheckIn(
            ticket_id=ticket.id,
            scanned_by=user_id,
            scan_time=datetime.utcnow()
        )

        db.session.add(log)

        db.session.commit()

        return log

    @staticmethod
    def scan(ticket_number, user_id=None):

        verification = CheckinService.verify_ticket(
            ticket_number
        )

        if not verification["success"]:

            return verification

        ticket = verification["ticket"]

        CheckinService.check_in(
            ticket,
            user_id
        )

        return {
            "success": True,
            "message": "Check-In Successful",
            "ticket": ticket
        }

    @staticmethod
    def get_event_checkins(event_id):

        return (
            CheckIn.query
            .join(Ticket)
            .filter(
                Ticket.event_id == event_id
            )
            .all()
        )