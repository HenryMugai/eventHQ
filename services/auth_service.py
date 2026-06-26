from flask_login import login_user
from flask_login import logout_user

from database.db import bcrypt

from models.user import User


class AuthService:

    @staticmethod
    def authenticate(email, password):

        email = email.strip().lower()

        user = User.query.filter_by(
            email=email
        ).first()

        if user is None:

            return None

        if not user.is_active:

            return None

        if not bcrypt.check_password_hash(
            user.password_hash,
            password
        ):

            return None

        return user

    @staticmethod
    def login(user, remember=False):

        login_user(
            user,
            remember=remember
        )

    @staticmethod
    def logout():

        logout_user()

    @staticmethod
    def hash_password(password):

        return bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

    @staticmethod
    def verify_password(user, password):

        return bcrypt.check_password_hash(
            user.password_hash,
            password
        )