import logging


class FORMATTERS:
    CLASSIC = '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'
    SHORT = '%(asctime)s %(levelname) [%(name)s] %(message)s'
    NO_TIME = '%(levelname)-8s [%(name)s] %(message)s'


class DT_FORMATTERS:
    CLASSIC = '%Y-%m-%d %H:%M:%S'
    TIME_FIST = '%H:%M:%S %Y-%m-%d'
    SHORT = '%y-%m-%d %H:%M:%S'
    TIME_ONLY = '%H:%M:%S'
    NO_DATE = TIME_ONLY


class LEVELS:
    CRITICAL = logging.CRITICAL
    FATAL = logging.FATAL
    ERROR = logging.ERROR
    WARNING = logging.WARNING
    INFO = logging.INFO
    DEBUG = logging.DEBUG


def get_file_handler(log_file_path, log_level=LEVELS.INFO,
                     formatter=FORMATTERS.CLASSIC, dt_formatter=DT_FORMATTERS.CLASSIC):
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(log_level)

    fmt = logging.Formatter(formatter)
    fmt.datefmt = dt_formatter

    file_handler.setFormatter(fmt)

    return file_handler


def get_console_handler(log_level=LEVELS.DEBUG,
                        formatter=FORMATTERS.CLASSIC, dt_formatter=DT_FORMATTERS.CLASSIC):
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    fmt = logging.Formatter(formatter)
    fmt.datefmt = dt_formatter

    console_handler.setFormatter(fmt)

    return console_handler


def get_logger(logger_name, console_handler=None, file_handler=None):
    if logger_name in logging.Logger.manager.loggerDict:
        return logging.Logger.manager.loggerDict[logger_name]

    if console_handler is None and file_handler is None:
        console_handler = get_console_handler()

    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    if console_handler is not None:
        logger.addHandler(console_handler)
    if file_handler is not None:
        logger.addHandler(file_handler)

    return logger
