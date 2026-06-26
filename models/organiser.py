from datetime import datetime

from database.db import db


class Organiser(db.Model):

    __tablename__ = "organisers"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id"),
        nullable=False
    )

    company_name = db.Column(
        db.String(255),
        nullable=False
    )

    contact_person = db.Column(
        db.String(255)
    )

    phone = db.Column(
        db.String(50)
    )

    email = db.Column(
        db.String(150)
    )

    website = db.Column(
        db.String(255)
    )

    address = db.Column(
        db.Text
    )

    logo = db.Column(
        db.String(255)
    )

    notes = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Relationships
    # ==========================================

    user = db.relationship(
        "User",
        back_populates="organiser"
    )

    events = db.relationship(
        "Event",
        back_populates="organiser",
        lazy=True,
        cascade="all, delete-orphan"
    )

    support_requests = db.relationship(
        "SupportRequest",
        back_populates="organiser",
        lazy=True,
        cascade="all, delete-orphan"
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def total_events(self):

        return len(self.events)

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<Organiser(id={self.id}, "
            f"company='{self.company_name}')>"
        )