from models.user import User
from database.db import db
from database.db import bcrypt


class UserService:

    @staticmethod
    def get_all():

        return User.query.order_by(
            User.full_name.asc()
        ).all()

    @staticmethod
    def get_by_id(user_id):

        return User.query.get(user_id)

    @staticmethod
    def get_by_email(email):

        return User.query.filter_by(
            email=email
        ).first()

    @staticmethod
    def create(
        full_name,
        email,
        phone,
        password,
        role
    ):

        password_hash = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            password_hash=password_hash,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def suspend(user):

        user.is_active = False

        db.session.commit()

    @staticmethod
    def activate(user):

        user.is_active = True

        db.session.commit()

    @staticmethod
    def reset_password(user, password):

        user.password_hash = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        db.session.commit()

    @staticmethod
    def delete(user):

        db.session.delete(user)

        db.session.commit()