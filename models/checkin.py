from database.db import db
from datetime import datetime


class CheckIn(db.Model):
    __tablename__ = "checkins"

    id = db.Column(db.BigInteger, primary_key=True)

    ticket_id = db.Column(
        db.BigInteger,
        db.ForeignKey("tickets.id"),
        nullable=False
    )

    scanned_by = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id")
    )

    scan_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    notes = db.Column(
        db.Text
    )

    def __repr__(self):
        return f"<CheckIn {self.id}>"