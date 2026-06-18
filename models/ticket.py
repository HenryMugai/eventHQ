from database.db import db
from datetime import datetime


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.BigInteger, primary_key=True)

    order_id = db.Column(
        db.BigInteger,
        db.ForeignKey("orders.id")
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
        default="valid"
    )

    ticket_source = db.Column(
        db.Enum(
            "online",
            "bulk_upload",
            "complimentary",
            "manual",
            name="ticket_source"
        ),
        default="online"
    )

    issued_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    checkins = db.relationship(
        "CheckIn",
        backref="ticket",
        lazy=True
    )

    def __repr__(self):
        return f"<Ticket {self.ticket_number}>"