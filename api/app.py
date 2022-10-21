#!/usr/bin/python3
"""
Flask Application
"""
from flask import Flask, jsonify
from api.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.errorhandler(404)
def error_handler(exception):
    """
    Handler Error 404
    """
    response = {"Error": "Not found"}
    return jsonify(response), 404


if __name__ == "__main__":
    """
    Main Function
    """
    app.run(host='0.0.0.0', port=5000, threaded=True)
