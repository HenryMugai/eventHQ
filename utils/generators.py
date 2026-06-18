import random
import string
from uuid import uuid4
from datetime import datetime


def generate_reference(prefix="EVHQ"):

    timestamp = datetime.now().strftime(
        "%Y%m%d%H%M%S"
    )

    random_part = ''.join(
        random.choices(
            string.digits,
            k=5
        )
    )

    return f"{prefix}-{timestamp}-{random_part}"


def generate_order_reference():

    return generate_reference(
        "ORD"
    )


def generate_payment_reference():

    return generate_reference(
        "PAY"
    )


def generate_ticket_number():

    year = datetime.now().year

    code = str(uuid4()).replace(
        "-",
        ""
    )[:8].upper()

    return f"EVHQ-{year}-{code}"


def generate_temp_password(length=8):

    characters = (
        string.ascii_letters +
        string.digits
    )

    return ''.join(
        random.choice(characters)
        for _ in range(length)
    )