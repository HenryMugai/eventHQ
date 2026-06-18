from flask import Blueprint

admin_bp = Blueprint(
    "admin",
    __name__,
    template_folder="../../templates/admin"
)

from . import dashboard
from . import events
from . import organisers
from . import users
from . import ticket_types
from . import tickets
from . import orders
from . import payments
from . import checkins
from . import reports
from . import exports
from . import categories
from . import support_requests
from . import notifications
from . import settings
from . import audit_logs