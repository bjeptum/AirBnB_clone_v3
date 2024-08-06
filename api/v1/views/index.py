#!/usr/bin/python3
"""Creating routes"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """ Creates route/status on object app_views"""
    return jsonify({"status": "OK"})
