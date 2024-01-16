from flask import render_template, request, redirect, flash, jsonify, url_for
from mock_eq import app

from mock_eq.common.decrypter import Decrypter
from mock_eq.common.pubsub import PubSub
from sdc.crypto.exceptions import InvalidTokenException, CryptoError

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
    if not (token:= request.args.get("token")):
        logger.error("No token passed")
        return render_template("errors/400-error.html", frontstage=app.config["FRONTSTAGE_URL"])

    try:
        decrypter = Decrypter(app.config["JSON_SECRET_KEYS"])
        payload = decrypter.decrypt(token)
    except (InvalidTokenException, CryptoError) as e:
        logger.error("An error happened when decrypting the token", error=e.value)
        return render_template("errors/400-error.html", frontstage=app.config["FRONTSTAGE_URL"])

    data = payload["survey_metadata"]["data"]

    receipt_url = url_for(
        "receipt",
        case_ref=data["case_ref"],
        case_id=payload["case_id"],
        party_id=data["user_id"],
        sds_dataset_id=data.get("sds_dataset_id"),
    )

    return render_template(
        "mock_eq_v3.html",
        title="Mock eQ v3",
        frontstage=app.config["FRONTSTAGE_URL"],
        receipt_url=receipt_url,
        payload=payload,
    )


@app.route("/receipt", methods=["GET"])
def receipt():
    pubsub_payload = {
        "caseRef": request.args.get("case_ref"),
        "caseId": request.args.get("case_id"),
        "inboundChannel": "OFFLINE",
        "partyId": request.args.get("party_id"),
    }
    if request.args.get("sds_dataset_id"):
        pubsub_payload["sdsDatasetId"] = request.args.get("sds_dataset_id")

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
