#!/usr/bin/python3
"""
Module that defines the Building class
"""
from models.base_model import BaseModel
from models import storage


class Building(BaseModel):
    """
    This class defines a building
    by various attributes
    """
    id_condominium = 0
    name_building = ""
    ruc = 0
    phone = 0
    email = ""
    description = ""
    floor = 0
    address = ""
    user_created = ""
    user_updated = ""


def buildings_get(id_condominium=None):
    """
    method that returns all the buildings
    within a condominium by their ID
    """
    list_result = []

    str_1 = "SELECT condominium.name, building.* FROM building INNER JOIN"
    str_2 = str_1 + " condominium ON building.id_condominium=condominium.id"
    str_3 = str_2 + " WHERE building.id_condominium={}".format(id_condominium)
    query = str_3 + " ORDER BY id DESC;"

    storage.cursor.execute(query)

    tupla = storage.cursor.fetchall()

    for dictionary in tupla:
        list_result.append(dictionary)

    return list_result


def building_get(building_id=None):
    """
    method that returns a building by its ID
    """
    str_1 = "SELECT condominium.name, building.* FROM building INNER JOIN"
    str_2 = str_1 + " condominium ON building.id_condominium=condominium.id"
    str_3 = str_2 + " WHERE building.id={}".format(building_id)
    query = str_3 + " ORDER BY id DESC;"

    storage.cursor.execute(query)

    tupla = storage.cursor.fetchall()

    for dictionary in tupla:
        return dictionary
