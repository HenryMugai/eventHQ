from flask import render_template

from middleware import admin_required

from models.notification import Notification

from . import admin_bp


@admin_bp.route("/notifications")
@admin_required
def notifications():

    notifications = (
        Notification.query
        .order_by(
            Notification.created_at.desc()
        )
        .all()
    )

    return render_template(
        "admin/notifications/index.html",
        notifications=notifications
    )