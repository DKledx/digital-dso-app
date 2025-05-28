import logging
import os
from datetime import datetime

def get_logger(name: str):
    logger = logging.getLogger(name)
    if not logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(name)s] [request_id=%(request_id)s] %(message)s"
        )
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        # File handler
        os.makedirs("logs", exist_ok=True)
        log_filename = f"logs/app_{datetime.now().strftime('%Y-%m-%d')}.log"
        fh = logging.FileHandler(log_filename)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.setLevel(logging.INFO)
    return logger