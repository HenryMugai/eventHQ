import os

from werkzeug.utils import secure_filename

from utils.constants import (
    ALLOWED_IMAGE_EXTENSIONS,
    ALLOWED_EXCEL_EXTENSIONS
)


def allowed_image(filename):

    return (
        "." in filename
        and
        filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_IMAGE_EXTENSIONS
    )


def allowed_excel(filename):

    return (
        "." in filename
        and
        filename.rsplit(
            ".",
            1
        )[1].lower()
        in ALLOWED_EXCEL_EXTENSIONS
    )


def save_image(
    file,
    upload_folder
):

    if not file:
        return None

    if not allowed_image(
        file.filename
    ):
        return None

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    filename = secure_filename(
        file.filename
    )

    filepath = os.path.join(
        upload_folder,
        filename
    )

    file.save(
        filepath
    )

    return filename


def save_excel(
    file,
    upload_folder
):

    if not file:
        return None

    if not allowed_excel(
        file.filename
    ):
        return None

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    filename = secure_filename(
        file.filename
    )

    filepath = os.path.join(
        upload_folder,
        filename
    )

    file.save(
        filepath
    )

    return filepath


def delete_file(filepath):

    if os.path.exists(filepath):

        os.remove(filepath)

        return True

    return False