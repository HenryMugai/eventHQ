from database.db import db
from datetime import datetime


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.BigInteger, primary_key=True)

    order_id = db.Column(
        db.BigInteger,
        db.ForeignKey("orders.id"),
        nullable=False
    )

    transaction_reference = db.Column(
        db.String(255)
    )

    payment_method = db.Column(
        db.Enum(
            "mpesa",
            "pesapal",
            "cash",
            "bank",
            name="payment_methods"
        )
    )

    amount = db.Column(
        db.Numeric(12, 2)
    )

    payment_status = db.Column(
        db.Enum(
            "pending",
            "paid",
            "failed",
            "refunded",
            name="payment_status"
        ),
        default="pending"
    )

    paid_at = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Payment {self.id}>"