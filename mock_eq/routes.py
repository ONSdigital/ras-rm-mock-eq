from flask import render_template, request
from mock_eq import app

from sdc.crypto.decrypter import decrypt
from sdc.crypto.key_store import KeyStore, validate_required_keys

import json

import logging
import structlog

from google.cloud import pubsub_v1

KEY_PURPOSE = "authentication"
logger = structlog.wrap_logger(logging.getLogger(__name__))


@app.route("/")
@app.route("/session", methods=['GET'])
def mock_eq():
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

    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print('seetting publisher up')
    publisher = PubSub(app.config)
    print('publishing...')
    publisher.publish(pubsub_payload)
    print('published')
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    return render_template('base.html', title='Mock eQ', frontstage=app.config["FRONTSTAGE_URL"])


class Decrypter:
    def __init__(self, json_secret_keys):
        keys = json.loads(json_secret_keys)
        validate_required_keys(keys, KEY_PURPOSE)
        self.key_store = KeyStore(keys)

    def decrypt(self, payload):
        """
        Decrypts the payload using the keystore values
        :param payload: the value to decrypt
        :return: string of decrypted payload
        """
        decrypted_json = decrypt(payload, key_store=self.key_store, key_purpose=KEY_PURPOSE)
        return decrypted_json


class PubSub:
    def __init__(self, config):
        self.project_id = config["GOOGLE_CLOUD_PROJECT"]
        self.topic_id = config["PUBSUB_TOPIC"]
        self.publisher = None

    def publish(self, json_payload):
        bound_logger = logger.bind(template_id="mock_eq", project_id=self.project_id, topic_id=self.topic_id)

        payload_str = json.dumps(json_payload)
        if self.publisher is None:
            self.publisher = pubsub_v1.PublisherClient()

        try:
            topic_path = self.publisher.topic_path(self.project_id, self.topic_id)
            print('topic path: ' + topic_path)
            bound_logger.info("About to publish to pubsub", topic_path=topic_path)
            future = self.publisher.publish(topic_path, data=payload_str.encode())

            msg_id = future.result()
            bound_logger.info("Publish succeeded", msg_id=msg_id)
        except TimeoutError:
            bound_logger.error("Publish to pubsub timed out", exc_info=True)
            raise
        except Exception:
            bound_logger.error("A non-timeout error was raised when publishing to pubsub", exc_info=True)
            raise
