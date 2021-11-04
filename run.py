import logging
import os

# If no APP_SETTINGS in environment variables use developer settings
# This has to run before triggering mock_eq.__init__.py
if not os.getenv("APP_SETTINGS"):
    os.environ["APP_SETTINGS"] = "DevelopmentConfig"

from structlog import wrap_logger  # NOQA

from mock_eq import app  # NOQA

logger = wrap_logger(logging.getLogger(__name__))


if __name__ == "__main__":
    # port = app.config["PORT"]
    port = 8080
    logger.info("Starting listening port: ", port=port)
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", port=int(port))
