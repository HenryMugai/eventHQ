from datetime import datetime

from database.db import db

from models.payment import Payment


class PaymentService:

    @staticmethod
    def create_payment(
        order_id,
        amount,
        payment_method,
        transaction_reference=None
    ):

        payment = Payment(
            order_id=order_id,
            amount=amount,
            payment_method=payment_method,
            transaction_reference=transaction_reference,
            payment_status="pending"
        )

        db.session.add(payment)
        db.session.commit()

        return payment

    @staticmethod
    def mark_paid(payment):

        payment.payment_status = "paid"

        payment.paid_at = datetime.utcnow()

        db.session.commit()

    @staticmethod
    def mark_failed(payment):

        payment.payment_status = "failed"

        db.session.commit()

    @staticmethod
    def mark_refunded(payment):

        payment.payment_status = "refunded"

        db.session.commit()

    @staticmethod
    def get_by_id(payment_id):

        return Payment.query.get(payment_id)

    @staticmethod
    def get_order_payments(order_id):

        return Payment.query.filter_by(
            order_id=order_id
        ).all()

    @staticmethod
    def total_event_revenue(event_id):

        total = 0

        payments = Payment.query.filter_by(
            payment_status="paid"
        ).all()

        for payment in payments:

            if payment.order and payment.order.event_id == event_id:
                total += float(payment.amount)

        return total