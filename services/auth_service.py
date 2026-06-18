from flask_login import login_user, logout_user
from database.db import bcrypt
from models.user import User


class AuthService:

    @staticmethod
    def authenticate(email, password):

        user = User.query.filter_by(
            email=email
        ).first()

        if not user:
            return None

        if not user.is_active:
            return None

        if bcrypt.check_password_hash(
            user.password_hash,
            password
        ):
            return user

        return None

    @staticmethod
    def login(user):

        login_user(user)

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