from flask import render_template

from flask_login import current_user

from middleware import organiser_required

from services.analytics_service import (
    AnalyticsService
)

from models.event import Event

from . import organiser_bp


@organiser_bp.route(
    "/events/<int:event_id>/analytics"
)
@organiser_required
def analytics(event_id):

    organiser = current_user.organiser

    event = Event.query.filter_by(
        id=event_id,
        organiser_id=organiser.id
    ).first_or_404()

    metrics = (
        AnalyticsService.event_metrics(
            event.id
        )
    )

    return render_template(
        "organiser/analytics/index.html",
        event=event,
        metrics=metrics
    )