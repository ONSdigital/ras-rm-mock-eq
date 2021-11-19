import os


class DevelopmentConfig(object):
    VERSION = "1.0.9"
    PORT = os.getenv("PORT", 8086)
    FRONTSTAGE_URL = os.getenv("FRONTSTAGE_URL", "http://localhost:8082/surveys/todo")
    JSON_SECRET_KEYS = os.getenv("JSON_SECRET_KEYS") or open("./tests/test_data/jwt-test-keys/test_key.json").read()
    PUBSUB_TOPIC = os.getenv("PUBSUB_TOPIC", "sdx-receipt-dev")
    GOOGLE_CLOUD_PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "ras-rm-dev")
