#!/usr/bin/python3
"""Blueprint Registration"""
from flask import Flask
from models import storage
from api.v1.views import app_views


""" Create variable app and register blueprint """
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """
    Handles teardown_appcontext()
    Function is alled automatically by Flask
    when application context tears down.
    """
    storage.close()


if __name__ == "__main__":
    """ Set host and port using env variables and default values"""
    import os

    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))

    """Run Flask server with specified configuration"""
    app.run(host=host, port=port, threaded=True)
