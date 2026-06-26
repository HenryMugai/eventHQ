from datetime import datetime

from database.db import db


class Order(db.Model):

    __tablename__ = "orders"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

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
        default=0.00,
        nullable=False
    )

    order_status = db.Column(
        db.Enum(
            "pending",
            "paid",
            "cancelled",
            "refunded",
            name="order_status"
        ),
        default="pending",
        nullable=False
    )

    source = db.Column(
        db.Enum(
            "online",
            "bulk_upload",
            "manual",
            name="order_source"
        ),
        default="online",
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Relationships
    # ==========================================

    event = db.relationship(
        "Event",
        back_populates="orders"
    )

    payments = db.relationship(
        "Payment",
        back_populates="order",
        lazy=True,
        cascade="all, delete-orphan"
    )

    tickets = db.relationship(
        "Ticket",
        back_populates="order",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def is_paid(self):

        return self.order_status == "paid"

    @property
    def ticket_count(self):

        return len(self.tickets)

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<Order(id={self.id}, "
            f"reference='{self.order_reference}')>"
        )