from database.db import db

from models.audit_log import AuditLog


def log_action(
    user_id,
    module_name,
    action_taken,
    record_id=None
):

    try:

        audit = AuditLog(
            user_id=user_id,
            module_name=module_name,
            action_taken=action_taken,
            record_id=record_id
        )

        db.session.add(audit)

        db.session.commit()

    except Exception as e:

        db.session.rollback()

        print(
            f"Audit Error: {e}"
        )