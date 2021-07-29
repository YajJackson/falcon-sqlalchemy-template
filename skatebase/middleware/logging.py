import logging
import logging.handlers
import os
import sys
from datetime import datetime
from logging import Logger


class LogManager:
    """
    Create an instance of logger for each request
    """

    include_file = True

    def __init__(self, include_file=True):
        self.include_file = include_file

    # Inspired by https://stackoverflow.com/a/41677596/8083126
    def create_logger(self) -> Logger:
        if self.include_file:
            file_path = sys.modules[__name__].__file__
            project_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
            log_location = project_path + "/logs/"
            if not os.path.exists(log_location):
                os.makedirs(log_location)

            current_time = datetime.now()
            current_date = current_time.strftime("%Y-%m-%d")
            file_name = current_date + ".log"
            file_location = log_location + file_name
            with open(file_location, "a+"):
                pass

        logger = logging.getLogger(__name__)
        format = "[%(asctime)s] [%(levelname)s] [%(message)s] [--> %(pathname)s [%(process)d]:]"

        if self.include_file:
            logging.basicConfig(
                format=format,
                filemode="a+",
                filename=file_location,
                level=logging.DEBUG,
            )
        else:
            logging.basicConfig(format=format, level=logging.DEBUG)

        return logger

    def process_resource(self, req, resp, resource, params):
        resource.logger = self.create_logger()
