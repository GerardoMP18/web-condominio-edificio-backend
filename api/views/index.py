#!/usr/bin/python3
"""
Module Index
"""
from api.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=['GET'],
                 strict_slashes=False)
def status():
    """
    Status of API
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats", methods=['GET'],
                 strict_slashes=False)
def number_register():
    """
    Method that returns a dictionary with all
    the tables and the number of their records
    """
    query = storage.count()

    return jsonify(query)
