#!/usr/bin/python3
"""
Blueprint for API
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix="/api")

from api.views.index import *
from api.views.users import *
from api.views.bulk_load import *
from api.views.login import *
from api.views.departaments import *
from api.views.buildings import *
from api.views.departaments_users import *
from api.views.condominiums import *
