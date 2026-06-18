import os
import logging

from flask import Flask, render_template

from config import Config

from database.db import (
    db,
    migrate,
    bcrypt,
    csrf,
    login_manager
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    csrf.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to continue."
    login_manager.login_message_category = "warning"

    # Import Models
    from models import (
        User,
        Organiser,
        Category,
        Event,
        TicketType,
        Order,
        Payment,
        Ticket,
        CheckIn,
        SupportRequest,
        Notification,
        AuditLog,
        Setting
    )

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Blueprints
    from routes.auth import auth_bp
    from routes.public import public_bp
    from routes.admin import admin_bp
    from routes.organiser import organiser_bp
    from routes.api import api_bp

    app.register_blueprint(auth_bp)

    app.register_blueprint(public_bp)

    app.register_blueprint(
        admin_bp,
        url_prefix="/admin"
    )

    app.register_blueprint(
        organiser_bp,
        url_prefix="/organiser"
    )

    app.register_blueprint(
        api_bp,
        url_prefix="/api"
    )

    # Create Upload Folders
    folders = [
        "uploads",
        "uploads/banners",
        "uploads/reports",
        "uploads/exports",
        "uploads/bulk_uploads",
        "uploads/temp",
        "uploads/tickets",
        "static/qr_codes",
        "logs"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    # Logging
    if not app.debug:

        logging.basicConfig(
            filename="logs/application.log",
            level=logging.INFO,
            format="%(asctime)s %(levelname)s: %(message)s"
        )

    # Health Check
    @app.route("/health")
    def health_check():

        return {
            "status": "ok",
            "application": "EventHQ"
        }

    # Error Handlers
    @app.errorhandler(404)
    def not_found(error):

        return render_template(
            "errors/404.html"
        ), 404

    @app.errorhandler(500)
    def internal_error(error):

        db.session.rollback()

        return render_template(
            "errors/500.html"
        ), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )