from sdc.crypto.decrypter import decrypt
from sdc.crypto.key_store import KeyStore, validate_required_keys

import json

KEY_PURPOSE = "authentication"


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
