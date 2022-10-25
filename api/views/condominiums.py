#!/usr/bin/python3
"""
Methods that handle all default
RestFul API actions for condominiums
"""
from api.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.condominium import Condominium
import re


@app_views.route("/condominiums", methods=['GET'],
                 strict_slashes=False)
def get_condominiums():
    """
    Method that returns the list of all condominium objects
    """
    list_condominiums = []
    condominiums = storage.all("condominium").values()

    for condominium in condominiums:
        list_condominiums.append(storage.to_dict("Condominium", condominium))

    return jsonify(list_condominiums)


@app_views.route("/condominiums/<condominium_id>", methods=['GET'],
                 strict_slashes=False)
def get_condominium_id(condominium_id=None):
    """
    Method that returns the values of
    a condominium by means of their ID
    """
    condominium = storage.get("condominium", int(condominium_id))
    if not condominium:
        abort(400, description="Condominium not found")

    return jsonify(storage.to_dict("Condominium", condominium))


@app_views.route("/condominiums/<condominium_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_condominium(condominium_id=None):
    """
    Method that deletes a condominium by their ID
    """
    condominium = storage.get("condominium", int(condominium_id))
    if not condominium:
        abort(400, description="Condominium not found")

    storage.delete("condominium", int(condominium_id))

    return jsonify({}), 200


@app_views.route("/condominiums", methods=['POST'],
                 strict_slashes=False)
def post_condominium():
    """
    Method that creates a condominium
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    obligatory = ["name", "ruc", "phone", "email", "address",
                  "landline", "user_created"]

    for needed in obligatory:
        if needed not in request.get_json():
            abort(400, description="Missing {}".format(needed))

    data = request.get_json()
    email_condominium = data["email"]

    regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    if not re.search(regex, email_condominium):
        abort(400, description="Invalid Email")

    comprobation = storage.verify('condominium', email_condominium)
    if comprobation:
        abort(400, description="Email has already been used")

    instance = Condominium(**data)
    instance.new('sp_add_condominium')

    return jsonify(instance.to_dict()), 201


@app_views.route('/condominiums/<condominium_id>', methods=['PUT'],
                 strict_slashes=False)
def put_condominium(condominium_id=None):
    """
    Method that updates a condominium by their ID
    """
    condominium = storage.get("condominium", int(condominium_id))
    if not condominium:
        abort(400, description="Condominium not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()

    if 'email' in data:
        email_condominium = data["email"]

        regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
        if not re.search(regex, email_condominium):
            abort(400, description="Invalid Email")

        comprobation = storage.verify('condominium', email_condominium)
        if comprobation:
            abort(400, description="Email has already been used")

    for key, value in data.items():
        for key_2 in condominium.keys():
            if key not in ignore:
                if key == key_2:
                    condominium[key] = value

    storage.update(condominium, condominium_id, "sp_update_condominium")
    return jsonify(storage.to_dict("Condominium", condominium)), 200
