from datetime import datetime

from database.db import db


class Event(db.Model):

    __tablename__ = "events"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id"),
        nullable=True
    )

    organiser_id = db.Column(
        db.BigInteger,
        db.ForeignKey("organisers.id"),
        nullable=True
    )

    event_name = db.Column(
        db.String(255),
        nullable=False
    )

    slug = db.Column(
        db.String(255),
        unique=True
    )

    short_description = db.Column(
        db.String(500)
    )

    description = db.Column(
        db.Text
    )

    venue = db.Column(
        db.String(255)
    )

    venue_address = db.Column(
        db.Text
    )

    google_maps_link = db.Column(
        db.String(500)
    )

    city = db.Column(
        db.String(100)
    )

    country = db.Column(
        db.String(100),
        default="Kenya"
    )

    banner_image = db.Column(
        db.String(255)
    )

    start_datetime = db.Column(
        db.DateTime,
        nullable=False
    )

    end_datetime = db.Column(
        db.DateTime,
        nullable=False
    )

    status = db.Column(
        db.Enum(
            "draft",
            "published",
            "closed",
            "cancelled",
            name="event_status"
        ),
        default="draft",
        nullable=False
    )

    is_featured = db.Column(
        db.Boolean,
        default=False
    )

    created_by = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Relationships
    # ==========================================

    category = db.relationship(
        "Category",
        back_populates="events"
    )

    organiser = db.relationship(
        "Organiser",
        back_populates="events"
    )

    creator = db.relationship(
        "User",
        foreign_keys=[created_by]
    )

    ticket_types = db.relationship(
        "TicketType",
        back_populates="event",
        lazy=True,
        cascade="all, delete-orphan"
    )

    orders = db.relationship(
        "Order",
        back_populates="event",
        lazy=True
    )

    tickets = db.relationship(
        "Ticket",
        back_populates="event",
        lazy=True
    )

    support_requests = db.relationship(
        "SupportRequest",
        back_populates="event",
        lazy=True
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def is_live(self):

        return self.status == "published"

    @property
    def duration(self):

        return self.end_datetime - self.start_datetime

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<Event(id={self.id}, "
            f"name='{self.event_name}')>"
        )