import logging.config
import yaml
import logging


def setup_logging() -> None:
    """Load logging configuration from YAML-file."""
    with open('config/logging.yaml') as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)