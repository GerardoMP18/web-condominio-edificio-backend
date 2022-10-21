#!/usr/bin/python3
"""
Module that defines the Building class
"""
from models.base_model import BaseModel


class Building(BaseModel):
    """
    This class defines a building
    by various attributes
    """
    id_condominium = 0
    name_building = ""
    description = ""
    floor = 0
    address = ""
    user_created = ""
    user_updated = ""
