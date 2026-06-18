from flask import Blueprint

organiser_bp = Blueprint(
    "organiser",
    __name__
)

from .dashboard import *
from .events import *
from .attendees import *
from .analytics import *
from .reports import *
from .downloads import *
from .support import *
from .profile import *