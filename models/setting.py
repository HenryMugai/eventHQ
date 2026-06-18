from database.db import db
from datetime import datetime


class Setting(db.Model):
    __tablename__ = "settings"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    setting_key = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    setting_value = db.Column(
        db.Text
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def __repr__(self):
        return f"<Setting {self.setting_key}>"