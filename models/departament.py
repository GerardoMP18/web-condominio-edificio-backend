#!/usr/bin/python3
"""
Module that defines the Departament class
"""
from models.base_model import BaseModel


class Departament(BaseModel):
    """
    This class defines a departament
    by various attributes
    """
    number_departament = 0
    id_district = 0
    id_building = 0
    number_bedrooms = 0
    floor = 0
    description = ""
    status = ""
    user_created = ""
    user_updated = ""
