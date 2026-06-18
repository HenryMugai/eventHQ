import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    # ==========================================
    # DATABASE
    # ==========================================

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://"
        f"{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ==========================================
    # FILE UPLOADS
    # ==========================================

    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    UPLOAD_FOLDER = "uploads"

    BANNER_FOLDER = "uploads/banners"

    EXPORT_FOLDER = "uploads/exports"

    REPORT_FOLDER = "uploads/reports"

    BULK_UPLOAD_FOLDER = "uploads/bulk_uploads"

    # ==========================================
    # MAIL SETTINGS
    # ==========================================

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT"))

    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # ==========================================
    # APP SETTINGS
    # ==========================================

    APP_NAME = "EventHQ"

    COMPANY_NAME = "EventHQ"

    ITEMS_PER_PAGE = 25