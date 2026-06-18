from database.db import db
from datetime import datetime


class TicketType(db.Model):
    __tablename__ = "ticket_types"

    id = db.Column(db.BigInteger, primary_key=True)

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
        default=0
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    sold = db.Column(
        db.Integer,
        default=0
    )

    max_per_order = db.Column(
        db.Integer,
        default=10
    )

    sales_start = db.Column(
        db.DateTime
    )

    sales_end = db.Column(
        db.DateTime
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<TicketType {self.name}>"