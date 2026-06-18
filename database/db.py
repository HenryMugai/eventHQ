# database/db.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

# ==================================================
# Database
# ==================================================

db = SQLAlchemy()

# ==================================================
# Migrations
# ==================================================

migrate = Migrate()

# ==================================================
# Authentication
# ==================================================

login_manager = LoginManager()

# ==================================================
# Security
# ==================================================

bcrypt = Bcrypt()

csrf = CSRFProtect()