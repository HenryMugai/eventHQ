from flask import render_template

from middleware import admin_required

from models.checkin import CheckIn

from . import admin_bp


@admin_bp.route("/checkins")
@admin_required
def checkins():

    checkins = CheckIn.query.order_by(
        CheckIn.scan_time.desc()
    ).all()

    return render_template(
        "admin/checkins/index.html",
        checkins=checkins
    )