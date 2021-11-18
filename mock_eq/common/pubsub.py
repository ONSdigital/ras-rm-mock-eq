from google.cloud import pubsub_v1
import json

import logging
import structlog

logger = structlog.wrap_logger(logging.getLogger(__name__))


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
