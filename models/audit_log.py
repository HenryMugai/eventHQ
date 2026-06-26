from datetime import datetime

from database.db import db


class AuditLog(db.Model):

    __tablename__ = "audit_logs"

    id = db.Column(
        db.BigInteger,
        primary_key=True
    )

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id"),
        nullable=True
    )

    module_name = db.Column(
        db.String(100),
        nullable=True
    )

    action_taken = db.Column(
        db.String(255),
        nullable=True
    )

    record_id = db.Column(
        db.BigInteger,
        nullable=True
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
        back_populates="audit_logs"
    )

    # ==========================================
    # Helper Methods
    # ==========================================

    def __repr__(self):

        return (
            f"<AuditLog(id={self.id}, "
            f"module='{self.module_name}', "
            f"action='{self.action_taken}')>"
        )