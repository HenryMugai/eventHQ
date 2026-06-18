from database.db import db
from datetime import datetime


class AuditLog(db.Model):
    __tablename__ = "audit_logs"

    id = db.Column(db.BigInteger, primary_key=True)

    user_id = db.Column(
        db.BigInteger,
        db.ForeignKey("users.id")
    )

    module_name = db.Column(
        db.String(100)
    )

    action_taken = db.Column(
        db.String(255)
    )

    record_id = db.Column(
        db.BigInteger
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<AuditLog {self.action_taken}>"