from flask import Flask, session
import os

app = Flask(__name__)

# Load app config
app_config = "config.{}".format(os.environ.get("APP_SETTINGS", "Config"))
app.config.from_object(app_config)

from mock_eq import routes
