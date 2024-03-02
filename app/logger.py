import logging
from datetime import datetime
from typing import Any, Dict

from pythonjsonlogger import jsonlogger

from app.config import settings


class CustomJsomFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]) -> None:
        super(CustomJsomFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            now = datetime.utcnow().strftime("%d.%m.%YT%H:%M:%S.%fZ")
            log_record["timestamp"] = now
        if log_record.get("level"):
            log_record["level"] = log_record["level"].upper()
        else:
            log_record["level"] = record.levelname


logger = logging.getLogger()
formatter = CustomJsomFormatter(
    "%(level)s %(timestamp)s %(message)s %(module)s %(funcName)s"
)
log_handler = logging.FileHandler("clinic.log")
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.setLevel(settings.LOG_LEVEL)
