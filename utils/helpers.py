from datetime import datetime


def format_currency(amount):

    try:
        return f"KES {float(amount):,.2f}"

    except Exception:
        return "KES 0.00"


def format_datetime(value):

    if not value:
        return ""

    return value.strftime(
        "%d %b %Y %I:%M %p"
    )


def format_date(value):

    if not value:
        return ""

    return value.strftime(
        "%d %b %Y"
    )


def safe_int(value, default=0):

    try:
        return int(value)

    except Exception:
        return default


def safe_float(value, default=0):

    try:
        return float(value)

    except Exception:
        return default


def now():

    return datetime.utcnow()