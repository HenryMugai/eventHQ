from sqlalchemy import func

from models.event import Event
from models.ticket import Ticket
from models.payment import Payment
from models.order import Order
from models.checkin import CheckIn


class AnalyticsService:

    @staticmethod
    def dashboard_metrics():

        total_events = Event.query.count()

        total_tickets = Ticket.query.count()

        total_checkins = CheckIn.query.count()

        total_revenue = (
            Payment.query.with_entities(
                func.sum(
                    Payment.amount
                )
            )
            .filter(
                Payment.payment_status == "paid"
            )
            .scalar()
        )

        return {
            "events": total_events,
            "tickets": total_tickets,
            "checkins": total_checkins,
            "revenue": total_revenue or 0
        }

    @staticmethod
    def event_metrics(event_id):

        tickets = Ticket.query.filter_by(
            event_id=event_id
        ).count()

        attendance = (
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
            "tickets": tickets,
            "attendance": attendance,
            "revenue": revenue
        }

    @staticmethod
    def organiser_metrics(organiser_id):

        events = Event.query.filter_by(
            organiser_id=organiser_id
        ).all()

        event_ids = [
            event.id
            for event in events
        ]

        ticket_count = (
            Ticket.query
            .filter(
                Ticket.event_id.in_(event_ids)
            )
            .count()
        )

        attendance_count = (
            CheckIn.query
            .join(Ticket)
            .filter(
                Ticket.event_id.in_(event_ids)
            )
            .count()
        )

        revenue = 0

        payments = Payment.query.all()

        for payment in payments:

            if (
                payment.order and
                payment.order.event_id in event_ids and
                payment.payment_status == "paid"
            ):
                revenue += float(payment.amount)

        return {
            "events": len(events),
            "tickets": ticket_count,
            "attendance": attendance_count,
            "revenue": revenue
        }