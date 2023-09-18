from flask import render_template, request, redirect, flash, jsonify
from mock_eq import app

from mock_eq.common.decrypter import Decrypter
from mock_eq.common.pubsub import PubSub

import logging
import structlog

logger = structlog.wrap_logger(logging.getLogger(__name__))


@app.route("/")
@app.route("/session", methods=["GET"])
def mock_eq():
    payload = request.args.get("token", None)
    if payload is None:
        logger.error("No payload passed from frontstage")
        flash("No payload passed from frontstage")
    return render_template("mock_eq.html", title="Mock eQ", frontstage=app.config["FRONTSTAGE_URL"], payload=payload)


@app.route("/v3/session", methods=["GET"])
def mock_eq_v3():
    # A similar endpoint to represent the EQ v3 site that now exists.  When it comes to the decryption in the /receipt
    # endpoint, the token should have the kid of key it needs to use.  If the keys have been set up correctly, it should
    # work for both eq and eq v3 without us having to do anything.
    payload = request.args.get("token", None)
    if payload is None:
        logger.error("No payload passed from frontstage")
        flash("No payload passed from frontstage")
    return render_template(
        "mock_eq_v3.html", title="Mock eQ v3", frontstage=app.config["FRONTSTAGE_URL"], payload=payload
    )


@app.route("/receipt", methods=["GET"])
def receipt():
    payload = request.args.get("token", None)

    try:
        json_secret_keys = app.config["JSON_SECRET_KEYS"]
        decrypter = Decrypter(json_secret_keys)

        json_payload = decrypter.decrypt(payload)

        logger.error("Payload received: " + str(json_payload))

        pubsub_payload = {
            "caseRef": json_payload["survey_metadata"]["data"]["case_ref"],
            "caseId": json_payload["case_id"],
            "inboundChannel": "OFFLINE",
            "partyId": json_payload["survey_metadata"]["data"]["user_id"]
        }

        if "sds_dataset_id" in json_payload["survey_metadata"]["data"]:
            pubsub_payload["sdsDatasetId"] = json_payload["survey_metadata"]["data"]["sds_dataset_id"]


    except Exception:
        logger.error("An error happened when decrypting the frontstage payload", exc_info=True)
        return render_template("errors/500-error.html", frontstage=app.config["FRONTSTAGE_URL"])

    publisher = PubSub(app.config)
    publisher.publish(pubsub_payload)
    return redirect(app.config["FRONTSTAGE_URL"])


@app.route("/info", methods=["GET"])
def get_info():
    info = {
        "name": "mock-eq",
        "status": "healthy",
    }
    return jsonify(info)
