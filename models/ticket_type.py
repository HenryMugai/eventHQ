from datetime import datetime

from database.db import db


class TicketType(db.Model):

    __tablename__ = "ticket_types"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    event_id = db.Column(
        db.BigInteger,
        db.ForeignKey("events.id"),
        nullable=False
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    price = db.Column(
        db.Numeric(12, 2),
        default=0.00,
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    sold = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    max_per_order = db.Column(
        db.Integer,
        default=10,
        nullable=False
    )

    sales_start = db.Column(
        db.DateTime
    )

    sales_end = db.Column(
        db.DateTime
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
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
        back_populates="ticket_types"
    )

    tickets = db.relationship(
        "Ticket",
        back_populates="ticket_type",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def available(self):

        return max(
            self.quantity - self.sold,
            0
        )

    @property
    def sold_out(self):

        return self.available == 0

    @property
    def sales_percentage(self):

        if self.quantity == 0:

            return 0

        return round(
            (self.sold / self.quantity) * 100,
            2
        )

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<TicketType(id={self.id}, "
            f"name='{self.name}')>"
        )