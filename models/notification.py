from datetime import datetime

from database.db import db


class Notification(db.Model):

    __tablename__ = "notifications"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(255),
        nullable=True
    )

    message = db.Column(
        db.Text,
        nullable=True
    )

    is_read = db.Column(
        db.Boolean,
        default=False,
        nullable=False
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
        back_populates="notifications"
    )

    # ==========================================
    # Helper Methods
    # ==========================================

    def mark_as_read(self):

        self.is_read = True

    def __repr__(self):

        return (
            f"<Notification(id={self.id}, "
            f"title='{self.title}', "
            f"read={self.is_read})>"
        )