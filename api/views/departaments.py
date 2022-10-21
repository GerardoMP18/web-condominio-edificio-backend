#!/usr/bin/python3
"""
Methods that handle all default
RestFul API actions for departaments
"""
from api.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.departament import Departament


@app_views.route("/buildings/<building_id>/departaments", methods=['GET'],
                 strict_slashes=False)
def get_departaments(building_id=None):
    """
    Method that returns the list of all departaments objects
    """
    building = storage.get("building", int(building_id))
    if not building:
        abort(400, description="Building not found")

    list_departaments = []
    departaments = storage.filters("departament", 'id_building',
                                   int(building_id))
    if not departaments:
        abort(400, description="Departaments not found")

    for departament in departaments:
        list_departaments.append(storage.to_dict("Departament", departament))

    return jsonify(list_departaments)


@app_views.route("/departaments/<departament_id>", methods=['GET'],
                 strict_slashes=False)
def get_departament_id(departament_id=None):
    """
    Method that returns the values of
    a departament by means of their ID
    """
    departament = storage.get("departament", int(departament_id))
    if not departament:
        abort(400, description="Departament not found")

    return jsonify(storage.to_dict("Departament", departament))


@app_views.route("/departaments/<departament_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_departament(departament_id=None):
    """
    Method that deletes a departament by their ID
    """
    departament = storage.get("departament", int(departament_id))
    if not departament:
        abort(400, description="Department not found")

    storage.delete("departament", int(departament_id))

    return jsonify({}), 200


@app_views.route("/buildings/<building_id>/departaments", methods=['POST'],
                 strict_slashes=False)
def post_departament(building_id=None):
    """
    Method that creates a departament
    """
    building = storage.get("building", int(building_id))
    if not building:
        abort(400, description="Building not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    obligatory = ["number_departament", "id_district", "id_building",
                  "number_bedrooms", "floor", "description", "status",
                  "user_created"]

    for needed in obligatory:
        if needed not in request.get_json():
            abort(400, description="Missing {}".format(needed))

    data = request.get_json()
    instance = Departament(**data)
    instance.new('sp_add_departament')

    return jsonify(instance.to_dict()), 201


@app_views.route('/departaments/<departament_id>', methods=['PUT'],
                 strict_slashes=False)
def put_departament(departament_id=None):
    """
    Method that updates a departament by their ID
    """
    departament = storage.get("departament", int(departament_id))
    if not departament:
        abort(400, description="Departament not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        for key_2 in departament.keys():
            if key not in ignore:
                if key == key_2:
                    departament[key] = value

    storage.update(departament, departament_id, "sp_update_departament")
    return jsonify(storage.to_dict("Departament", departament)), 200
