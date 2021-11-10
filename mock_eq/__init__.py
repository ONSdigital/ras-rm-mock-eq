from flask import Flask, session
import os

app = Flask(__name__)

from mock_eq import routes
