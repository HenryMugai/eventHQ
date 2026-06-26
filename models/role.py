from datetime import datetime

from database.db import db


class Role(db.Model):

    __tablename__ = "roles"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    description = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Relationships
    # ==========================================

    users = db.relationship(
        "User",
        back_populates="role",
        lazy=True
    )

    # ==========================================
    # Helper Properties
    # ==========================================

    @property
    def total_users(self):

        return len(self.users)

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<Role(id={self.id}, "
            f"name='{self.name}')>"
        )