from flask import render_template, redirect, request
from mock_eq import app

from sdc.crypto.decrypter import decrypt
from sdc.crypto.key_store import KeyStore, validate_required_keys

import json

import logging

KEY_PURPOSE = "authentication"
log = logging.getLogger()
logging.basicConfig()


@app.route("/")
@app.route("/session", methods=['GET'])
def mock_eq():
    payload = request.args.get('token', None)

    json_secret_keys = app.config["JSON_SECRET_KEYS"]
    print('here')
    print('here')
    print(json_secret_keys)
    # decrypter = Decrypter(json_secret_keys)

    # payload_json = decrypter.decrypt(payload)
    print('here')
    print('here')
    print('payload_json')
    # print(payload_json)
    return render_template('base.html', title='Mock eQ')


@app.route("/receipt")
def receipt():
    return redirect(app.config["FRONTSTAGE_URL"])


class Decrypter:
    def __init__(self, json_secret_keys):
        keys = json.loads(json_secret_keys)
        # print(keys)
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
