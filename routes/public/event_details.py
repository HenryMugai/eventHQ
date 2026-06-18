from flask import render_template
from flask import abort

from models.event import Event

from . import public_bp


@public_bp.route("/events/<int:event_id>")
def event_details(event_id):

    event = Event.query.get(
        event_id
    )

    if not event:

        abort(404)

    return render_template(
        "public/event_details.html",
        event=event
    )