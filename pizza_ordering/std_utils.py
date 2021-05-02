import json
import logging


def create_dumps(filename, data):
    with open(f"{filename}.json", "w") as f:
        f.write(json.dumps(data))


def test_error():
    logger = logging.getLogger(__name__)
    logger.error("Test error in utils general")
