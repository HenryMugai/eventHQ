from datetime import datetime

from flask_login import UserMixin

from database.db import db


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    role_id = db.Column(
        db.Integer,
        db.ForeignKey("roles.id"),
        nullable=False
    )

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100)
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    phone = db.Column(
        db.String(30)
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True,
        nullable=False
    )

    last_login = db.Column(
        db.DateTime
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

    role = db.relationship(
        "Role",
        back_populates="users"
    )

    organiser = db.relationship(
        "Organiser",
        back_populates="user",
        uselist=False
    )

    notifications = db.relationship(
        "Notification",
        back_populates="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    audit_logs = db.relationship(
        "AuditLog",
        back_populates="user",
        lazy=True,
        cascade="all, delete-orphan"
    )

    checkins = db.relationship(
        "CheckIn",
        foreign_keys="CheckIn.scanned_by",
        lazy=True
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def full_name(self):

        return (
            f"{self.first_name} "
            f"{self.last_name or ''}"
        ).strip()

    @property
    def is_admin(self):

        return (
            self.role is not None
            and self.role.name == "admin"
        )

    @property
    def is_organiser(self):

        return (
            self.role is not None
            and self.role.name == "organiser"
        )

    @property
    def is_gate_agent(self):

        return (
            self.role is not None
            and self.role.name == "gate_agent"
        )

    # ==========================================
    # Flask-Login
    # ==========================================

    def get_id(self):

        return str(self.id)

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<User(id={self.id}, "
            f"email='{self.email}')>"
        )