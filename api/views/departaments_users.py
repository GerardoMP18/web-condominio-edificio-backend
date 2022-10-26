#!/usr/bin/python3
"""
Methods that handle all default
RestFul API actions for departaments_users
"""
from api.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.departament_user import Departament_User, filter_departament
from models.departament_user import delete_dpt_user
from models.user import verify_dpto_owner, verify_dpto_tenant


@app_views.route("/users/<user_id>/departaments", methods=['GET'],
                 strict_slashes=False)
def get_departaments_users(user_id=None):
    """
    Method that returns the list of all departaments_users objects
    """
    list_departaments = []

    user = storage.get("user", int(user_id))

    if not user:
        abort(400, description="User not found")

    departaments = filter_departament(user_id)

    for departament in departaments:
        list_departaments.append(storage.to_dict("Departament", departament))

    return jsonify(list_departaments)


@app_views.route("/users/<user_id>/departaments/<departament_id>",
                 methods=['DELETE'], strict_slashes=False)
def delete_departament_user(user_id, departament_id):
    """
    Method that deletes a departament_user by their ID
    """
    user = storage.get("user", int(user_id))
    if not user:
        abort(400, description="User not found")

    departament = storage.get("departament", int(departament_id))
    if not departament:
        abort(400, description="Departament not found")

    delete_dpt_user(int(user_id), int(departament_id))

    return jsonify({}), 200


@app_views.route("/users/<user_id>/departaments/<departament_id>",
                 methods=['POST'], strict_slashes=False)
def post_departament_user(user_id, departament_id):
    """
    Method that link departament user
    """
    data_result = {}

    user = storage.get("user", int(user_id))
    if not user:
        abort(400, description="User not found")

    departament = storage.get("departament", int(departament_id))
    if not departament:
        abort(400, description="Departament not found")

    # ----------------------------------------------------------
    role = user["id_role"]
    if role == 1:
        abort(400, description="Admins cannot be assigned to a department")

    elif role == 2:
        if not verify_dpto_owner(departament_id):
            abort(400, description="Departament already has an Owner")

    elif role == 3:
        verify = verify_dpto_tenant(departament_id)
        if verify is None:
            abort(400, description="Need to assign an owner")

        elif verify is False:
            abort(400, description="Departament already has an Tenant")
    # -----------------------------------------------------------

    data_result["id_user"] = user_id
    data_result["id_departament"] = departament_id

    if not request.get_json():
        abort(400, description="Not a JSON")

    if "user_created" not in request.get_json():
        abort(400, description="Missing user_created")

    data = request.get_json()
    data_result.update(data)
    instance = Departament_User(**data_result)
    instance.new('sp_add_departament_user')

    return jsonify(instance.to_dict()), 201
