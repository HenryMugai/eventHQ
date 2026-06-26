from datetime import datetime

from database.db import db


class SupportRequest(db.Model):

    __tablename__ = "support_requests"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    organiser_id = db.Column(
        db.BigInteger,
        db.ForeignKey("organisers.id"),
        nullable=False
    )

    event_id = db.Column(
        db.BigInteger,
        db.ForeignKey("events.id"),
        nullable=True
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
        default="open",
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

    organiser = db.relationship(
        "Organiser",
        back_populates="support_requests"
    )

    event = db.relationship(
        "Event",
        back_populates="support_requests"
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def is_open(self):

        return self.status in [
            "open",
            "in_progress"
        ]

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<SupportRequest(id={self.id}, "
            f"status='{self.status}')>"
        )