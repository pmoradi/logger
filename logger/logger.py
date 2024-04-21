import logging
import json
from logging.handlers import RotatingFileHandler

class Json_Formatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'pathname': record.pathname,
            'lineno': record.lineno,
            'funcName': record.funcName
        }
        return json.dumps(log_record)

class Logger:
    def __init__(self, name, log_file):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
        file_handler.setLevel(logging.DEBUG)

        # Create a JSON formatter
        json_formatter = Json_Formatter()

        file_handler.setFormatter(json_formatter)

        self.logger.addHandler(file_handler)

def get_logger(name):
    logger_dict = logging.Logger.manager.loggerDict
    logger_names = logger_dict.keys()
    registered_names = list(logger_names)
    if name in registered_names:
        return logging.getLogger(name)
    else:
        raise Exception("The given logger's name has not been registered.")
