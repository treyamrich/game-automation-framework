import logging

class Logger:
    """
    This class encapsulates the logic for creating a logger using the python logging module.
    """
    def __init__(self, name: str, severity_level: str = 'warning'):
        """
        name: the name of the logger, which should be the name of the folder that contains the script
        severity_level: str specifies the logging severity level. All log msgs of the level and above will be logged.
        """
        self.logger = logging.getLogger(name)
        self._set_log_level(severity_level)
        
        log_file_path =  f'{name}.log'
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler(log_file_path)
        c_handler.setFormatter(formatter)
        f_handler.setFormatter(formatter)

        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)
        
    def _set_log_level(self, severity_level: str):
        if severity_level == 'debug':
            self.logger.setLevel(logging.DEBUG)
        elif severity_level == 'info':
            self.logger.setLevel(logging.INFO)
        elif severity_level == 'error':
            self.logger.setLevel(logging.ERROR)
        elif severity_level == 'critical':
            self.logger.setLevel(logging.CRITICAL)
        else: # Default level
            self.logger.setLevel(logging.WARNING)
            
    # Echo the logging methods
    def debug(self, msg: str):
        self.logger.debug(msg)
    def info(self, msg: str):
        self.logger.info(msg)
    def warning(self, msg: str):
        self.logger.warning(msg)
    def error(self, msg: str):
        self.logger.error(msg)
    def critical(self, msg: str):
        self.logger.critical(msg)