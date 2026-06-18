from flask import render_template

from flask_login import current_user

from middleware import organiser_required

from services.analytics_service import (
    AnalyticsService
)

from . import organiser_bp


@organiser_bp.route("/")
@organiser_bp.route("/dashboard")
@organiser_required
def dashboard():

    organiser = current_user.organiser

    metrics = (
        AnalyticsService.organiser_metrics(
            organiser.id
        )
    )

    return render_template(
        "organiser/dashboard.html",
        metrics=metrics,
        organiser=organiser
    )