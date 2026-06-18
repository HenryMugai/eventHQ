import re


def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return re.match(
        pattern,
        email
    ) is not None


def validate_phone(phone):

    phone = str(phone).strip()

    if len(phone) < 10:
        return False

    return True


def validate_password(password):

    if len(password) < 8:
        return False

    return True


def validate_required(value):

    if value is None:
        return False

    if str(value).strip() == "":
        return False

    return True


def validate_positive_number(value):

    try:

        value = float(value)

        return value >= 0

    except Exception:

        return False