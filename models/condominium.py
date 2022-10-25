#!/usr/bin/python3
"""
Module that defines the Condominium class
"""
from models.base_model import BaseModel


class Condominium(BaseModel):
    """
    This class defines a condominium
    by various attributes
    """
    name = ""
    ruc = 0
    phone = 0
    email = ""
    address = ""
    landline = 0
    description = ""
    user_created = ""
    user_updated = ""
