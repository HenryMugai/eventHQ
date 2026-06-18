from flask import render_template
from flask import request

from models.event import Event
from models.category import Category

from . import public_bp


@public_bp.route("/events")
def events():

    category_id = request.args.get(
        "category"
    )

    query = Event.query.filter_by(
        status="published"
    )

    if category_id:

        query = query.filter_by(
            category_id=category_id
        )

    events = query.order_by(
        Event.start_datetime.asc()
    ).all()

    categories = Category.query.order_by(
        Category.name.asc()
    ).all()

    return render_template(
        "public/events.html",
        events=events,
        categories=categories
    )