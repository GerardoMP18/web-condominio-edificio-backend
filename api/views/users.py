#!/usr/bin/python3
"""
Methods that handle all default
RestFul API actions for users
"""
from api.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.user import User, roles_get
import re


@app_views.route("/owners", methods=['GET'],
                 strict_slashes=False)
def get_owners():
    """
    GET method that returns all owners
    """
    list_owners = []
    owners = roles_get(2)

    for owner in owners:
        list_owners.append(storage.to_dict("Owner", owner))

    return jsonify(list_owners)


@app_views.route("/tenants", methods=['GET'],
                 strict_slashes=False)
def get_tenants():
    """
    GET method that returns all tenants
    """
    list_tenants = []
    tenants = roles_get(3)

    for tenant in tenants:
        list_tenants.append(storage.to_dict("Tenant", tenant))

    return jsonify(list_tenants)


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
        abort(400, description="User not found")

    return jsonify(storage.to_dict("User", user))


@app_views.route("/users/<user_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id=None):
    """
    Method that deletes a user by their ID
    """
    user = storage.get("user", int(user_id))
    if not user:
        abort(400, description="User not found")

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

    obligatory = ["first_name", "last_name", "id_document_type",
                  "number_document", "email", "password",
                  "phone", "birth_date", "id_role"]

    for needed in obligatory:
        if needed not in request.get_json():
            abort(400, description="Missing {}".format(needed))

    data = request.get_json()
    email_user = data["email"]

    regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    if not re.search(regex, email_user):
        abort(400, description="Invalid Email")

    comprobation = storage.verify('user', email_user)
    if comprobation:
        abort(400, description="Email has already been used")

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
        abort(400, description="User not found")

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()

    if 'email' in data:
        email_user = data["email"]

        regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
        if not re.search(regex, email_user):
            abort(400, description="Invalid Email")

        comprobation = storage.verify('user', email_user)
        if comprobation:
            abort(400, description="Email has already been used")

    for key, value in data.items():
        for key_2 in user.keys():
            if key not in ignore:
                if key == key_2:
                    user[key] = value

    storage.update(user, user_id, "sp_update_user")
    return jsonify(storage.to_dict("User", user)), 200
