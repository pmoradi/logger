import logging
from logging.handlers import TimedRotatingFileHandler

class Logger:
    def __init__(self, logger_name, log_file, format:logging.Formatter=None) -> None:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # Create a timed rotating file handler
        file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=30)        # Set the logging level
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter
        if format:
            formatter = format
        else:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', '%H:%M:%S')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)
        self.logger = logger
    
    def debug(self, message):
        self.logger.debug(message)
    def info(self, message):
        self.logger.info(message)
    def error(self, message):
        self.logger.error(message)
