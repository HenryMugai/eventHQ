from database.db import db
from datetime import datetime


class SupportRequest(db.Model):
    __tablename__ = "support_requests"

    id = db.Column(db.BigInteger, primary_key=True)

    organiser_id = db.Column(
        db.BigInteger,
        db.ForeignKey("organisers.id"),
        nullable=False
    )

    event_id = db.Column(
        db.BigInteger,
        db.ForeignKey("events.id")
    )

    subject = db.Column(
        db.String(255)
    )

    message = db.Column(
        db.Text
    )

    status = db.Column(
        db.Enum(
            "open",
            "in_progress",
            "resolved",
            "closed",
            name="support_status"
        ),
        default="open"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )