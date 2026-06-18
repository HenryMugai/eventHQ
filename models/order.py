from app import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.BigInteger, primary_key=True)

    order_reference = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    event_id = db.Column(
        db.BigInteger,
        db.ForeignKey("events.id"),
        nullable=False
    )

    customer_name = db.Column(
        db.String(255),
        nullable=False
    )

    customer_email = db.Column(
        db.String(150)
    )

    customer_phone = db.Column(
        db.String(50)
    )

    total_amount = db.Column(
        db.Numeric(12, 2),
        default=0
    )

    order_status = db.Column(
        db.Enum(
            "pending",
            "paid",
            "cancelled",
            "refunded",
            name="order_status"
        ),
        default="pending"
    )

    source = db.Column(
        db.Enum(
            "online",
            "bulk_upload",
            "manual",
            name="order_source"
        ),
        default="online"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    payments = db.relationship(
        "Payment",
        backref="order",
        lazy=True
    )

    tickets = db.relationship(
        "Ticket",
        backref="order",
        lazy=True
    )

    def __repr__(self):
        return f"<Order {self.order_reference}>"