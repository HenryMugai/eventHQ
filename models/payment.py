from datetime import datetime

from database.db import db


class Payment(db.Model):

    __tablename__ = "payments"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

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
        db.Numeric(12, 2),
        nullable=True
    )

    payment_status = db.Column(
        db.Enum(
            "pending",
            "paid",
            "failed",
            "refunded",
            name="payment_status"
        ),
        default="pending",
        nullable=False
    )

    paid_at = db.Column(
        db.DateTime
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Relationships
    # ==========================================

    order = db.relationship(
        "Order",
        back_populates="payments"
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def is_paid(self):

        return self.payment_status == "paid"

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<Payment(id={self.id}, "
            f"status='{self.payment_status}', "
            f"amount={self.amount})>"
        )