from flask import render_template, request, redirect, flash
from mock_eq import app
from pathlib import Path

from mock_eq.common.decrypter import Decrypter
from mock_eq.common.pubsub import PubSub

import logging
import structlog
import json

logger = structlog.wrap_logger(logging.getLogger(__name__))

_health_check = {}
if Path("git_info").exists():
    with open("git_info") as io:
        _health_check = json.loads(io.read())


@app.route("/")
@app.route("/session", methods=['GET'])
def mock_eq():
    payload = request.args.get('token', None)
    if payload is None:
        logger.error("No payload passed from frontstage")
        flash("No payload passed from frontstage")
    return render_template('base.html', title='Mock eQ', frontstage=app.config["FRONTSTAGE_URL"], payload=payload)


@app.route("/receipt", methods=["GET"])
def receipt():
    payload = request.args.get('token', None)

    try:
        json_secret_keys = app.config["JSON_SECRET_KEYS"]
        decrypter = Decrypter(json_secret_keys)

        json_payload = decrypter.decrypt(payload)
        pubsub_payload = {
            "caseRef": json_payload["case_ref"],
            "caseId": json_payload["case_id"],
            "inboundChannel": "OFFLINE",
            "partyId": json_payload["user_id"]
        }
    except Exception:
        logger.error("An error happend when decrypting the frontstage payload", exc_info=True)
        return render_template("errors/5000-error.html")

    publisher = PubSub(app.config)
    publisher.publish(pubsub_payload)
    return redirect(app.config["FRONTSTAGE_URL"])
