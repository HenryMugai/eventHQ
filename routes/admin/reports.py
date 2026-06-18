from flask import render_template

from middleware import admin_required

from models.event import Event

from services.report_service import (
    ReportService
)

from . import admin_bp


@admin_bp.route("/reports")
@admin_required
def reports():

    events = Event.query.all()

    return render_template(
        "admin/reports/index.html",
        events=events
    )


@admin_bp.route(
    "/reports/event/<int:event_id>"
)
@admin_required
def event_report(event_id):

    report = ReportService.event_summary(
        event_id
    )

    return render_template(
        "admin/reports/event.html",
        report=report
    )