from flask import render_template

from models.event import Event

from . import public_bp


@public_bp.route("/")
def home():

    featured_events = Event.query.filter_by(
        status="published",
        is_featured=True
    ).limit(6).all()

    upcoming_events = Event.query.filter_by(
        status="published"
    ).order_by(
        Event.start_datetime.asc()
    ).limit(12).all()

    return render_template(
        "public/home.html",
        featured_events=featured_events,
        upcoming_events=upcoming_events
    )