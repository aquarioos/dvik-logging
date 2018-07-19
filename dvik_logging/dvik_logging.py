import logging

_LINE_FORMATS = {
    'classic': '%(asctime)s %(levelname)-8s [%(name)s] %(message)s',
    'short': '%(asctime)s %(levelname) [%(name)s] %(message)s',
    'no_time': '%(levelname)-8s [%(name)s] %(message)s',
}

_DT_FORMATS = {
    'classic': '%Y-%m-%d %H:%M:%S',
    'time_first': '%H:%M:%S %Y-%m-%d',
    'short': '%y-%m-%d %H:%M:%S',
    'time_only': '%H:%M:%S',
    'no_date': '%H:%M:%S',
}

_LOG_LEVELS = {
    'critical': logging.CRITICAL,
    'fatal': logging.FATAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG,
}


def _get_file_handler(log_file_path, log_level='info', line_format='classic', dt_format='classic'):
    """Tworzy uchwyt loggera do pliku.

    Args:
        log_file_path (str): ścieżka do pliku
        log_level (str): poziom logowania, domyślnie "info"
        line_formatter (str): format logowanej linii, domyślnie "classic"
        dt_formatter (str): format logowanej daty, domyślnie "classic"

    Returns:
        logging.FileHandler: uchwyt loggera do pliku
    """

    try:
        log_level = _LOG_LEVELS[log_level]
    except KeyError:
        raise ValueError('nie ma poziomu logowania "{}"'.format(log_level))

    try:
        line_format = _LINE_FORMATS[line_format]
    except KeyError:
        raise ValueError('nie ma formatu "{}"'.format(line_format))

    try:
        dt_format = _DT_FORMATS[dt_format]
    except KeyError:
        raise ValueError('nie ma formatu daty "{}"'.format(dt_format))

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(log_level)

    fmt = logging.Formatter(line_format)
    fmt.datefmt = dt_format

    file_handler.setFormatter(fmt)

    return file_handler


def _get_console_handler(log_level='debug', line_format='classic', dt_format='classic'):
    """Tworzy uchwyt loggera do konsoli.

    Args:
        log_level (str, optional): poziom logowania, domyślnie "debug"
        line_formatter (str, optional): format logowanej linii, domyślnie "classic"
        dt_formatter (str, optional): format logowanej daty, domyślnie "classic"

    Returns:
        logging.StreamHandler: uchwyt loggera do konsoli

    Raises:
        ValueError: jeśli log_level, formatter lub dt_formatter nie istnieje
    """

    try:
        log_level = _LOG_LEVELS[log_level]
    except KeyError:
        raise ValueError('nie ma poziomu logowania "{}"'.format(log_level))

    try:
        line_format = _LINE_FORMATS[line_format]
    except KeyError:
        raise ValueError('nie ma formatu "{}"'.format(line_format))

    try:
        dt_format = _DT_FORMATS[dt_format]
    except KeyError:
        raise ValueError('nie ma formatu daty "{}"'.format(dt_format))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    fmt = logging.Formatter(line_format)
    fmt.datefmt = dt_format

    console_handler.setFormatter(fmt)

    return console_handler


def add_file_handler(logger_name, file_path, log_level='info', line_format='classic', dt_format='classic'):
    """Dodaje do loggera o podanej nazwie uchwyt do pliku o podanych parametrach.

    Args:
        logger_name (str): nazwa loggera
        file_path (str): ścieżka do pliku logów
        log_level (str, optional): poziom logowania, domyślnie "info"
        line_formatter (str, optional): format logowanej linii, domyślnie "classic"
        dt_formatter (str, optional): format logowanej daty, domyślnie "classic"

    Raises:
        ValueError: jeśli nie ma loggera o podanej nazwie lub parametr słownikowy jest niepoprawny
    """

    try:
        logger = logging.Logger.manager.loggerDict[logger_name]
    except KeyError:
        raise ValueError('logger o nazwie {} nie istnieje'.format(logger_name))

    try:
        log_level = _LOG_LEVELS[log_level]
    except KeyError:
        raise ValueError('nie ma poziomu logowania "{}"'.format(log_level))

    try:
        line_format = _LINE_FORMATS[line_format]
    except KeyError:
        raise ValueError('nie ma formatu "{}"'.format(line_format))

    try:
        dt_format = _DT_FORMATS[dt_format]
    except KeyError:
        raise ValueError('nie ma formatu daty "{}"'.format(dt_format))

    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(log_level)

    fmt = logging.Formatter(line_format)
    fmt.datefmt = dt_format

    file_handler.setFormatter(fmt)

    logger.addHandler(file_handler)


def add_console_handler(logger_name, log_level='debug', line_format='classic', dt_format='classic'):
    """Dodaje do loggera o podanej nazwie uchwyt do konsoli o podanych parametrach.

    Args:
        logger_name (str): nazwa loggera
        log_level (str, optional): poziom logowania, domyślnie "debug"
        line_formatter (str, optional): format logowanej linii, domyślnie "classic"
        dt_formatter (str, optional): format logowanej daty, domyślnie "classic"

    Raises:
        ValueError: jeśli nie ma loggera o podanej nazwie lub parametr słownikowy jest niepoprawny
    """

    try:
        logger = logging.Logger.manager.loggerDict[logger_name]
    except KeyError:
        raise KeyError('logger o nazwie {} nie istnieje'.format(logger_name))

    try:
        log_level = _LOG_LEVELS[log_level]
    except KeyError:
        raise ValueError('nie ma poziomu logowania "{}"'.format(log_level))

    try:
        line_format = _LINE_FORMATS[line_format]
    except KeyError:
        raise ValueError('nie ma formatu "{}"'.format(line_format))

    try:
        dt_format = _DT_FORMATS[dt_format]
    except KeyError:
        raise ValueError('nie ma formatu daty "{}"'.format(dt_format))

    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    fmt = logging.Formatter(line_format)
    fmt.datefmt = dt_format

    console_handler.setFormatter(fmt)

    logger.addHandler(console_handler)


def clear_handlers(logger_name):
    """Czyści uchwyty (handlery) w loggerze o podanej nazwie.

    Args:
        logger_name (str): nazwa loggera, w którym mają być wyczyszczone uchwyty (handlery)

    Raises:
        ValueError: jeśli logger o podanej nazwie nie istnieje
    """

    try:
        for h in logging.Logger.manager.loggerDict[logger_name].handlers:
            if isinstance(h, logging.FileHandler):
                h.flush()
                h.close()
        logging.Logger.manager.loggerDict[logger_name].handlers = []
    except KeyError:
        raise ValueError('logger "{}" nie istnieje'.format(logger_name))


def create_logger(logger_name):
    """Tworzy logger o podanej nazwie (jeśli nie istnieje).

    Args:
        logger_name (str): nazwa loggera

    Returns:
        logging.Logger: utworzony logger
    """

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    return logger


def get_logger(logger_name, ch_params=None, fh_params=None):
    """Pobiera logger. Jeśli logger o podanej nazwie już istnieje, to zwraca istniejący.

    Args:
        logger_name (str): nazwa loggera
        ch_params (dict): słownik z parametrami console handlera
        fh_params (dict): słownik z parametrami file handlera

    Returns:
        logging.Logger: obiekt loggera

    Raises:
        KeyError: jeśli nie podano ścieżki do pliku logów
    """

    if logger_name in logging.Logger.manager.loggerDict:
        return logging.Logger.manager.loggerDict[logger_name]

    logger = create_logger(logger_name)

    if ch_params is not None:
        add_console_handler(logger_name,
                            log_level=ch_params.get('log_level', 'debug'),
                            line_format=ch_params.get('line_format', 'classic'),
                            dt_format=ch_params.get('dt_format', 'classic'))

    if fh_params is not None:
        try:
            add_file_handler(logger_name, fh_params['file_path'],
                             log_level=fh_params.get('log_level', 'info'),
                             line_format=fh_params.get('line_format', 'classic'),
                             dt_format=fh_params.get('dt_format', 'classic'))
        except KeyError:
            raise KeyError('nie podano ścieżki do pliku logów')

    return logger
