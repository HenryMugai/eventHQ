from flask import render_template

from middleware import admin_required

from models.audit_log import AuditLog

from . import admin_bp


@admin_bp.route("/audit-logs")
@admin_required
def audit_logs():

    logs = AuditLog.query.order_by(
        AuditLog.created_at.desc()
    ).all()

    return render_template(
        "admin/audit_logs/index.html",
        logs=logs
    )