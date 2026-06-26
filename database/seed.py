from database.db import db
from database.db import bcrypt

from models.role import Role
from models.user import User


def seed_roles():

    roles = [

        (
            "admin",
            "Platform Administrator"
        ),

        (
            "organiser",
            "Event Organiser"
        ),

        (
            "gate_agent",
            "Gate Agent"
        )

    ]

    for name, description in roles:

        exists = Role.query.filter_by(
            name=name
        ).first()

        if exists is None:

            db.session.add(

                Role(
                    name=name,
                    description=description
                )

            )

    db.session.commit()


def seed_admin():

    seed_roles()

    admin = User.query.filter_by(
        email="admin@eventhq.com"
    ).first()

    if admin:

        print("Administrator already exists.")

        return

    admin_role = Role.query.filter_by(
        name="admin"
    ).first()

    admin = User(

        role_id=admin_role.id,

        first_name="System",

        last_name="Administrator",

        email="admin@eventhq.com",

        phone="0700000000",

        password_hash=bcrypt.generate_password_hash(
            "Admin@123"
        ).decode("utf-8"),

        is_active=True

    )

    db.session.add(admin)

    db.session.commit()

    print("Default administrator created successfully.")