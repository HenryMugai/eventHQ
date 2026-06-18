from flask import Blueprint

auth_bp = Blueprint(
    "auth",
    __name__
)

from .login import *
from .logout import *
from .forgot_password import *
from .profile import *