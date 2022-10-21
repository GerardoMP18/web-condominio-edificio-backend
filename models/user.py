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
    last_name = ""
    id_document_type = 0
    number_document = 0
    email = ""
    password = ""
    phone = 0
    birth_date = ""
