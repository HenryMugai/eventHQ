from flask import render_template

from middleware import admin_required

from models.setting import Setting

from . import admin_bp


@admin_bp.route("/settings")
@admin_required
def settings():

    settings = Setting.query.all()

    return render_template(
        "admin/settings/index.html",
        settings=settings
    )