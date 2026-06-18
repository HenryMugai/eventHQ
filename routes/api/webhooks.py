from flask import request
from flask import jsonify

from models.payment import Payment

from services.payment_service import (
    PaymentService
)

from . import api_bp


@api_bp.route(
    "/webhooks/pesapal",
    methods=["POST"]
)
def pesapal_webhook():

    data = request.json

    transaction_reference = data.get(
        "transaction_reference"
    )

    payment = Payment.query.filter_by(
        transaction_reference=transaction_reference
    ).first()

    if payment:

        PaymentService.mark_paid(
            payment
        )

    return jsonify({
        "success": True
    })