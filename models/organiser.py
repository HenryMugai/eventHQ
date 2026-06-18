from app import db
from datetime import datetime


class Organiser(db.Model):
    __tablename__ = "organisers"

    id = db.Column(db.BigInteger, primary_key=True)

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id"),
        nullable=False
    )

    company_name = db.Column(
        db.String(255),
        nullable=False
    )

    contact_person = db.Column(db.String(255))

    phone = db.Column(db.String(50))

    email = db.Column(db.String(150))

    website = db.Column(db.String(255))

    address = db.Column(db.Text)

    logo = db.Column(db.String(255))

    notes = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    events = db.relationship(
        "Event",
        backref="organiser",
        lazy=True
    )

    def __repr__(self):
        return f"<Organiser {self.company_name}>"