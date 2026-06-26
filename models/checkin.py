from datetime import datetime

from database.db import db


class CheckIn(db.Model):

    __tablename__ = "checkins"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    ticket_id = db.Column(
        db.BigInteger,
        db.ForeignKey("tickets.id"),
        nullable=False
    )

    scanned_by = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id"),
        nullable=True
    )

    scan_time = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    notes = db.Column(
        db.Text
    )

    # ==========================================
    # Relationships
    # ==========================================

    ticket = db.relationship(
        "Ticket",
        back_populates="checkins"
    )

    scanner = db.relationship(
        "User",
        foreign_keys=[scanned_by]
    )

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<CheckIn(id={self.id}, "
            f"ticket_id={self.ticket_id})>"
        )