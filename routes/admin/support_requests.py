from flask import render_template

from middleware import admin_required

from models.support_request import (
    SupportRequest
)

from . import admin_bp


@admin_bp.route("/support-requests")
@admin_required
def support_requests():

    requests = (
        SupportRequest.query
        .order_by(
            SupportRequest.created_at.desc()
        )
        .all()
    )

    return render_template(
        "admin/support_requests/index.html",
        requests=requests
    )