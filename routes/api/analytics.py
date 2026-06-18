from flask import jsonify

from services.analytics_service import (
    AnalyticsService
)

from . import api_bp


@api_bp.route(
    "/analytics/dashboard"
)
def dashboard_metrics():

    metrics = (
        AnalyticsService.dashboard_metrics()
    )

    return jsonify(metrics)


@api_bp.route(
    "/analytics/event/<int:event_id>"
)
def event_metrics(event_id):

    metrics = (
        AnalyticsService.event_metrics(
            event_id
        )
    )

    return jsonify(metrics)


@api_bp.route(
    "/analytics/organiser/<int:organiser_id>"
)
def organiser_metrics(
    organiser_id
):

    metrics = (
        AnalyticsService.organiser_metrics(
            organiser_id
        )
    )

    return jsonify(metrics)