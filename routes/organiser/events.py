from flask import render_template

from flask_login import current_user

from middleware import organiser_required

from models.event import Event

from . import organiser_bp


@organiser_bp.route("/events")
@organiser_required
def events():

    organiser = current_user.organiser

    events = Event.query.filter_by(
        organiser_id=organiser.id
    ).order_by(
        Event.start_datetime.desc()
    ).all()

    return render_template(
        "organiser/events/index.html",
        events=events
    )


@organiser_bp.route(
    "/events/<int:event_id>"
)
@organiser_required
def event_details(event_id):

    organiser = current_user.organiser

    event = Event.query.filter_by(
        id=event_id,
        organiser_id=organiser.id
    ).first_or_404()

    return render_template(
        "organiser/events/details.html",
        event=event
    )