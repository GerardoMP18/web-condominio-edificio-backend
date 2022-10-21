#!/usr/bin/python3
"""
Module that defines the Departament_user class
"""
from models.base_model import BaseModel
from models import storage


class Departament_User(BaseModel):
    """
    This class defines a departament_user
    by various attributes
    """
    id_user = 0
    id_departament = 0
    user_created = ""
    user_updated = ""


def filter_departament(id_user=None):
    """
    Method that filters the departments assigned by a user
    """
    list_result = []

    str_1 = "SELECT u.first_name, u.last_name, d.number_departament, "
    str_2 = str_1 + "d.id_district, d.id_building, d.number_bedrooms, d.floor,"
    str_3 = str_2 + " d.description, d.status, d.created_at, d.updated_at, "
    str_4 = str_3 + "d.user_created, d.user_updated FROM departament AS d "
    str_5 = str_4 + "INNER JOIN departament_user AS du ON d.id="
    str_6 = str_5 + "du.id_departament INNER JOIN user AS u ON du.id_user="
    query = str_6 + "u.id WHERE u.id={};".format(id_user)

    storage.cursor.execute(query)

    tupla = storage.cursor.fetchall()

    for dictionary in tupla:
        list_result.append(dictionary)

    return list_result


def delete_dpt_user(id_user, id_departament):
    """
    Method that removes department assignments from users
    """
    str_1 = "DELETE FROM departament_user WHERE id_user"
    query = str_1 + "={} AND id_departament={};".format(id_user,
                                                        id_departament)
    storage.cursor.execute(query)
    storage.db.commit()
