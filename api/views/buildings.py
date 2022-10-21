#!/usr/bin/python3
"""
Methods that handle all default
RestFul API actions for buildings
"""
from api.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.building import Building


@app_views.route("/condominiums/<condominium_id>/buildings", methods=['GET'],
                 strict_slashes=False)
def get_buildings(condominium_id=None):
    """
    Method that returns the list of all buildings objects
    """
    condominium = storage.get("condominium", int(condominium_id))
    if not condominium:
        abort(400, description="Condominium not found")

    list_buildings = []
    buildings = storage.filters("building", 'id_condominium',
                                int(condominium_id))
    if not buildings:
        abort(400, description="Buildings not found")

    for building in buildings:
        list_buildings.append(storage.to_dict("Building", building))

    return jsonify(list_buildings)


@app_views.route("/buildings/<building_id>", methods=['GET'],
                 strict_slashes=False)
def get_building_id(building_id=None):
    """
    Method that returns the values of
    a building by means of their ID
    """
    building = storage.get("building", int(building_id))
    if not building:
        abort(400, description="Building not found")

    return jsonify(storage.to_dict("Building", building))


@app_views.route("/buildings/<building_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_building(building_id=None):
    """
    Method that deletes a building by their ID
    """
    building = storage.get("building", int(building_id))
    if not building:
        abort(400, description="Building not found")

    storage.delete("building", int(building_id))

    return jsonify({}), 200


@app_views.route("/condominiums/<condominium_id>/buildings", methods=['POST'],
                 strict_slashes=False)
def post_building(condominium_id=None):
    """
    Method that creates a building
    """
    condominium = storage.get("condominium", int(condominium_id))
    if not condominium:
        abort(400, description="Condominium not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    obligatory = ["id_condominium", "name_building", "description",
                  "floor", "address", "user_created"]

    for needed in obligatory:
        if needed not in request.get_json():
            abort(400, description="Missing {}".format(needed))

    data = request.get_json()
    instance = Building(**data)
    instance.new('sp_add_building')

    return jsonify(instance.to_dict()), 201


@app_views.route('/buildings/<building_id>', methods=['PUT'],
                 strict_slashes=False)
def put_building(building_id=None):
    """
    Method that updates a building by their ID
    """
    building = storage.get("building", int(building_id))
    if not building:
        abort(400, description="Building not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        for key_2 in building.keys():
            if key not in ignore:
                if key == key_2:
                    building[key] = value

    storage.update(building, building_id, "sp_update_building")
    return jsonify(storage.to_dict("Building", building)), 200
