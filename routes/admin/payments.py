from flask import render_template

from middleware import admin_required

from models.payment import Payment

from . import admin_bp


@admin_bp.route("/payments")
@admin_required
def payments():

    payments = Payment.query.order_by(
        Payment.created_at.desc()
    ).all()

    return render_template(
        "admin/payments/index.html",
        payments=payments
    )