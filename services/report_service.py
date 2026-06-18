from models.event import Event
from models.ticket import Ticket
from models.payment import Payment
from models.checkin import CheckIn


class ReportService:

    @staticmethod
    def event_summary(event_id):

        event = Event.query.get(event_id)

        tickets = Ticket.query.filter_by(
            event_id=event_id
        ).count()

        checked_in = (
            CheckIn.query
            .join(Ticket)
            .filter(
                Ticket.event_id == event_id
            )
            .count()
        )

        revenue = 0

        payments = Payment.query.all()

        for payment in payments:

            if (
                payment.order and
                payment.order.event_id == event_id and
                payment.payment_status == "paid"
            ):
                revenue += float(payment.amount)

        return {
            "event": event,
            "tickets": tickets,
            "checked_in": checked_in,
            "revenue": revenue
        }

    @staticmethod
    def attendee_report(event_id):

        tickets = Ticket.query.filter_by(
            event_id=event_id
        ).all()

        data = []

        for ticket in tickets:

            data.append({
                "ticket_number": ticket.ticket_number,
                "name": ticket.attendee_name,
                "email": ticket.attendee_email,
                "phone": ticket.attendee_phone,
                "status": ticket.status
            })

        return data

    @staticmethod
    def financial_report(event_id):

        total_revenue = 0

        payments = Payment.query.all()

        for payment in payments:

            if (
                payment.order and
                payment.order.event_id == event_id and
                payment.payment_status == "paid"
            ):
                total_revenue += float(payment.amount)

        return {
            "event_id": event_id,
            "revenue": total_revenue
        }