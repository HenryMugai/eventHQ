from flask import render_template

from middleware import admin_required

from services.analytics_service import AnalyticsService

from . import admin_bp


@admin_bp.route("/")
@admin_bp.route("/dashboard")
@admin_required
def dashboard():

    metrics = AnalyticsService.dashboard_metrics()

    return render_template(
        "admin/dashboard.html",
        metrics=metrics
    )