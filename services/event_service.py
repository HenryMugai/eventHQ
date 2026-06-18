from database.db import db

from models.event import Event


class EventService:

    @staticmethod
    def get_all():

        return Event.query.order_by(
            Event.start_datetime.desc()
        ).all()

    @staticmethod
    def get_published():

        return Event.query.filter_by(
            status="published"
        ).all()

    @staticmethod
    def get_by_id(event_id):

        return Event.query.get(
            event_id
        )

    @staticmethod
    def create(**kwargs):

        event = Event(
            **kwargs
        )

        db.session.add(
            event
        )

        db.session.commit()

        return event

    @staticmethod
    def update(event, data):

        for key, value in data.items():

            setattr(
                event,
                key,
                value
            )

        db.session.commit()

        return event

    @staticmethod
    def publish(event):

        event.status = "published"

        db.session.commit()

    @staticmethod
    def close(event):

        event.status = "closed"

        db.session.commit()

    @staticmethod
    def cancel(event):

        event.status = "cancelled"

        db.session.commit()

    @staticmethod
    def delete(event):

        db.session.delete(
            event
        )

        db.session.commit()