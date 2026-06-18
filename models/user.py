from app import db
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.BigInteger, primary_key=True)

    full_name = db.Column(db.String(255), nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    phone = db.Column(db.String(50))

    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(
        db.Enum(
            "admin",
            "organiser",
            "gate_agent",
            name="user_roles"
        ),
        nullable=False,
        default="organiser"
    )

    is_active = db.Column(db.Boolean, default=True)

    email_verified_at = db.Column(db.DateTime)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    organiser = db.relationship(
        "Organiser",
        backref="user",
        uselist=False
    )

    def __repr__(self):
        return f"<User {self.email}>"