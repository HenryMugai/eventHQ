from flask import render_template
from flask import request
from flask import redirect
from flask import flash
from flask import url_for

from flask_login import current_user

from middleware import organiser_required

from database.db import db

from models.support_request import (
    SupportRequest
)

from . import organiser_bp


@organiser_bp.route(
    "/support",
    methods=["GET", "POST"]
)
@organiser_required
def support():

    organiser = current_user.organiser

    if request.method == "POST":

        support_request = (
            SupportRequest(
                organiser_id=organiser.id,
                event_id=request.form.get(
                    "event_id"
                ),
                subject=request.form.get(
                    "subject"
                ),
                message=request.form.get(
                    "message"
                )
            )
        )

        db.session.add(
            support_request
        )

        db.session.commit()

        flash(
            "Request submitted successfully.",
            "success"
        )

        return redirect(
            url_for(
                "organiser.support"
            )
        )

    requests = (
        SupportRequest.query
        .filter_by(
            organiser_id=organiser.id
        )
        .order_by(
            SupportRequest.created_at.desc()
        )
        .all()
    )

    return render_template(
        "organiser/support/index.html",
        requests=requests
    )