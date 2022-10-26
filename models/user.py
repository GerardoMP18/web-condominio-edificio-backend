#!/usr/bin/python3
"""
Module that defines the User class
"""
from models.base_model import BaseModel
import models


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
    id_role = 0


def roles_get(role_id=None):
    """
    Method that returns all owners or tenants
    """
    list_result = []

    str_1 = "SELECT user.first_name, user.last_name, building.name_building,"
    str_2 = str_1 + " departament.floor, departament.number_departament FROM"
    str_3 = str_2 + " user LEFT JOIN departament_user ON user.id ="
    str_4 = str_3 + " departament_user.id_user LEFT JOIN departament ON"
    str_5 = str_4 + " departament_user.id_departament=departament.id LEFT JOIN"
    str_6 = str_5 + " building ON departament.id_building = building.id WHERE"
    query = str_6 + " id_role={};".format(role_id)

    models.storage.cursor.execute(query)

    tupla = models.storage.cursor.fetchall()

    for dictionary in tupla:
        list_result.append(dictionary)

    return list_result


def verify_dpto_owner(id_departament=None):
    """
    Method that checks if a department already has an owner
    """
    str_1 = "SELECT user.first_name, user.id_role FROM departament_user"
    str_2 = str_1 + " INNER JOIN user ON departament_user.id_user ="
    str_3 = str_2 + " user.id WHERE departament_user."
    query = str_3 + "id_departament={} AND id_role = 2;".format(id_departament)

    models.storage.cursor.execute(query)

    tupla = models.storage.cursor.fetchall()

    if len(tupla) == 0:
        return True

    for dictionary in tupla:
        if dictionary["id_role"] == 2:
            return False

    return True


def verify_dpto_tenant(id_departament=None):
    """
    Method that checks if a department already has an tenant
    """
    str_1 = "SELECT user.first_name, user.id_role FROM departament_user"
    str_2 = str_1 + " INNER JOIN user ON departament_user.id_user ="
    str_3 = str_2 + " user.id WHERE departament_user."
    query = str_3 + "id_departament={};".format(id_departament)

    models.storage.cursor.execute(query)

    tupla = models.storage.cursor.fetchall()

    if len(tupla) == 0:
        return None

    for dictionary in tupla:
        if dictionary["id_role"] == 3:
            return False

    return True
