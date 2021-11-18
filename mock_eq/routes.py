from flask import render_template, request, redirect
from mock_eq import app

from mock_eq.common.decrypter import Decrypter
from mock_eq.common.pubsub import PubSub

import logging
import structlog

logger = structlog.wrap_logger(logging.getLogger(__name__))


@app.route("/")
@app.route("/session", methods=['GET'])
def mock_eq():
    payload = request.args.get('token', None)
    return render_template('base.html', title='Mock eQ', frontstage=app.config["FRONTSTAGE_URL"], payload=payload)


@app.route("/receipt", methods=["GET"])
def receipt():
    payload = request.args.get('token', None)

    json_secret_keys = app.config["JSON_SECRET_KEYS"]
    decrypter = Decrypter(json_secret_keys)

    json_payload = decrypter.decrypt(payload)
    pubsub_payload = {
        "caseRef": json_payload["case_ref"],
        "caseId": json_payload["case_id"],
        "inboundChannel": "OFFLINE",
        "partyId": json_payload["user_id"]
    }

    publisher = PubSub(app.config)
    publisher.publish(pubsub_payload)
    return redirect(app.config["FRONTSTAGE_URL"])
