from app import db
from datetime import datetime


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.BigInteger, primary_key=True)

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id")
    )

    organiser_id = db.Column(
        db.BigInteger,
        db.ForeignKey("organisers.id")
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
        default="draft"
    )

    is_featured = db.Column(
        db.Boolean,
        default=False
    )

    created_by = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    ticket_types = db.relationship(
        "TicketType",
        backref="event",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Event {self.event_name}>"