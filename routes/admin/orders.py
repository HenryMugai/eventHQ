from flask import render_template

from middleware import admin_required

from models.order import Order

from . import admin_bp


@admin_bp.route("/orders")
@admin_required
def orders():

    orders = Order.query.order_by(
        Order.created_at.desc()
    ).all()

    return render_template(
        "admin/orders/index.html",
        orders=orders
    )