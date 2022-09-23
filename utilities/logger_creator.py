import logging
import sys
import os
from typing import Tuple
def map_logging_level(level_text: str) ->int:
    '''
    Map str logging level to logging level integer
    :param level_text: a str represent the logging level, warning, info, error, debug.
    :return: an integer code in python logging represent the logging level
    '''
    assert type(level_text) == str

    if level_text == 'warning':
        level = logging.WARNING
    elif level_text == 'info':
        level = logging.INFO
    elif level_text == 'error':
        level = logging.ERROR
    elif level_text == 'debug':
        level = logging.DEBUG
    else:
        raise ValueError('Level {} for logging is not supported'.format(level_text))
    return level

def logger_creator(
        filepath: str,
        format: str = '%(asctime)s %(levelname)s %(funcName)s %(message)s',
        handler_level: str = 'info'
)->Tuple[logging.Logger, logging.Logger]:
    '''
    Create a looger and a warning loggers
    :param filepath: str log file path
    :param format: logging format str
    :param handler_level: logging level
    :return: a tuple consists of a regular logger and a warning logger
    '''

    logging.captureWarnings(True)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    warnings_logger = logging.getLogger("py.warnings")
    formatter = logging.Formatter(format)

    parent_path = os.path.dirname(filepath)
    if parent_path != '':
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)

    level = map_logging_level(handler_level)
    file_handler = logging.FileHandler(filepath, mode='w')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(level)

    if (logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    if (warnings_logger.hasHandlers()):
        warnings_logger.handlers.clear()
    warnings_logger.addHandler(file_handler)
    warnings_logger.addHandler(stream_handler)
    return logger, warnings_logger