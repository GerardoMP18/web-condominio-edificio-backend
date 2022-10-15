#!/usr/bin/python3
"""
Methods that handle all default
RestFul API actions for users
"""
from api.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@app_views.route("/users", methods=['GET'],
                 strict_slashes=False)
def get_users():
    """
    Method that returns the list of all user objects
    """
    list_users = []
    users = storage.all("user").values()

    for user in users:
        list_users.append(storage.to_dict("User", user))

    return jsonify(list_users)


@app_views.route("/users/<user_id>", methods=['GET'],
                 strict_slashes=False)
def get_user_id(user_id=None):
    """
    Method that returns the values of
    a user by means of their ID
    """
    user = storage.get("user", int(user_id))
    if not user:
        abort(404)

    return jsonify(storage.to_dict("User", user))


@app_views.route("/users/<user_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id=None):
    """
    Method that deletes a user by their ID
    """
    user = storage.get("user", int(user_id))
    if not user:
        abort(404)

    storage.delete("user", int(user_id))

    return jsonify({}), 200


@app_views.route("/users", methods=['POST'],
                 strict_slashes=False)
def post_user():
    """
    Method that creates a user
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    obligatory = ["first_name", "id_document_type", "last_name",
                  "email", "password", "number_document",
                  "phone", "birth_date"]

    for needed in obligatory:
        if needed not in request.get_json():
            abort(400, description="Missing {}".format(needed))

    data = request.get_json()
    instance = User(**data)
    instance.new('sp_add_user')

    return jsonify(instance.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id=None):
    """
    Method that updates a user by their ID
    """
    user = storage.get("user", int(user_id))
    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        for key_2 in user.keys():
            if key not in ignore:
                if key == key_2:
                    user[key] = value

    storage.update(user, user_id)
    return jsonify(storage.to_dict("User", user)), 200
