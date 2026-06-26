from datetime import datetime

from database.db import db


class Ticket(db.Model):

    __tablename__ = "tickets"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    order_id = db.Column(
        db.BigInteger,
        db.ForeignKey("orders.id"),
        nullable=True
    )

    event_id = db.Column(
        db.BigInteger,
        db.ForeignKey("events.id"),
        nullable=False
    )

    ticket_type_id = db.Column(
        db.BigInteger,
        db.ForeignKey("ticket_types.id"),
        nullable=False
    )

    ticket_number = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    qr_code = db.Column(
        db.String(255)
    )

    attendee_name = db.Column(
        db.String(255),
        nullable=False
    )

    attendee_email = db.Column(
        db.String(150)
    )

    attendee_phone = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.Enum(
            "valid",
            "used",
            "cancelled",
            "refunded",
            name="ticket_status"
        ),
        default="valid",
        nullable=False
    )

    ticket_source = db.Column(
        db.Enum(
            "online",
            "bulk_upload",
            "complimentary",
            "manual",
            name="ticket_source"
        ),
        default="online",
        nullable=False
    )

    issued_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Relationships
    # ==========================================

    order = db.relationship(
        "Order",
        back_populates="tickets"
    )

    event = db.relationship(
        "Event",
        back_populates="tickets"
    )

    ticket_type = db.relationship(
        "TicketType",
        back_populates="tickets"
    )

    checkins = db.relationship(
        "CheckIn",
        back_populates="ticket",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def has_checked_in(self):

        return len(self.checkins) > 0

    @property
    def latest_checkin(self):

        if not self.checkins:

            return None

        return max(
            self.checkins,
            key=lambda checkin: checkin.scan_time
        )

    @property
    def is_valid(self):

        return self.status == "valid"

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<Ticket(id={self.id}, "
            f"number='{self.ticket_number}')>"
        )