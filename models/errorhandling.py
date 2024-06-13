import logging

class ErrorHandling:
    def __init__(self, logger_name):
        self.logger = logging.getLogger(logger_name)

    def log_error(self, error_message, error_code=500):
        self.logger.error(f"Error {error_code}: {error_message}")

    def handle_error(self, error, error_code=500):
        self.log_error(str(error), error_code)
        raise Exception(f"Error {error_code}: {error}")

    def handle_exception(self, exception, error_code=500):
        self.log_error(str(exception), error_code)
        raise exception

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

 errorHandler = ErrorHandling('ClassicCollectionHub')