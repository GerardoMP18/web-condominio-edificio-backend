#!/usr/bin/python3
"""
Module that defines the User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines a user
    by various attributes
    """
    first_name = ""
    id_document_type = 0
    last_name = ""
    email = ""
    password = ""
    number_document = 0
    phone = 0
    birth_date = ""
