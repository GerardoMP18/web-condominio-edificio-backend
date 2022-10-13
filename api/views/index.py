#!/usr/bin/python3
"""
Module Index
"""
from api.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """
    Status of API
    """
    return jsonify({"status": "OK"})
