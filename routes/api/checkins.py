from flask import jsonify
from flask import request

from flask_login import current_user

from services.checkin_service import (
    CheckinService
)

from . import api_bp


@api_bp.route(
    "/checkin",
    methods=["POST"]
)
def checkin():

    data = request.json

    ticket_number = data.get(
        "ticket_number"
    )

    result = CheckinService.scan(
        ticket_number,
        current_user.id if current_user.is_authenticated else None
    )

    return jsonify(result)