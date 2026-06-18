from database.db import db

from models.organiser import Organiser
from models.user import User

from services.user_service import UserService


class OrganiserService:

    @staticmethod
    def get_all():

        return Organiser.query.order_by(
            Organiser.company_name.asc()
        ).all()

    @staticmethod
    def get_by_id(organiser_id):

        return Organiser.query.get(
            organiser_id
        )

    @staticmethod
    def create(
        company_name,
        contact_person,
        email,
        phone,
        password
    ):

        user = UserService.create(
            full_name=contact_person,
            email=email,
            phone=phone,
            password=password,
            role="organiser"
        )

        organiser = Organiser(
            user_id=user.id,
            company_name=company_name,
            contact_person=contact_person,
            email=email,
            phone=phone
        )

        db.session.add(
            organiser
        )

        db.session.commit()

        return organiser

    @staticmethod
    def suspend(organiser):

        user = User.query.get(
            organiser.user_id
        )

        user.is_active = False

        db.session.commit()

    @staticmethod
    def activate(organiser):

        user = User.query.get(
            organiser.user_id
        )

        user.is_active = True

        db.session.commit()

    @staticmethod
    def delete(organiser):

        user = User.query.get(
            organiser.user_id
        )

        db.session.delete(
            organiser
        )

        db.session.delete(
            user
        )

        db.session.commit()