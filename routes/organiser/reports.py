from flask import render_template

from flask_login import current_user

from middleware import organiser_required

from services.report_service import (
    ReportService
)

from models.event import Event

from . import organiser_bp


@organiser_bp.route(
    "/events/<int:event_id>/reports"
)
@organiser_required
def reports(event_id):

    organiser = current_user.organiser

    event = Event.query.filter_by(
        id=event_id,
        organiser_id=organiser.id
    ).first_or_404()

    report = ReportService.event_summary(
        event.id
    )

    return render_template(
        "organiser/reports/index.html",
        event=event,
        report=report
    )