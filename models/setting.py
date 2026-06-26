from datetime import datetime

from database.db import db


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
        onupdate=datetime.utcnow,
        nullable=False
    )

    # ==========================================
    # Helper Methods
    # ==========================================

    @staticmethod
    def get(key, default=None):

        setting = Setting.query.filter_by(
            setting_key=key
        ).first()

        if setting:

            return setting.setting_value

        return default

    @staticmethod
    def set(key, value):

        setting = Setting.query.filter_by(
            setting_key=key
        ).first()

        if setting is None:

            setting = Setting(
                setting_key=key,
                setting_value=value
            )

            db.session.add(setting)

        else:

            setting.setting_value = value

        db.session.commit()

        return setting

    def __repr__(self):

        return (
            f"<Setting(key='{self.setting_key}')>"
        )