"""
DVikLogging
~~~~~~~~~~~

Pakiet pisany w ramach projektu DVik. Jest to dodatkowa warstwa na bibliotekę logging. Umożliwi łatwe pobranie i skonfigurowanie obiektu loggera wraz z odpowiednimi uchwytami (handlerami).

Użycie:

    ch = get_console_handler(level=LEVELS.DEBUG, formatter=FORMATTERS.TIME_ONLY, dt_formatter=DT_FORMATTERS.SHORT)
    fh = get_file_handler(log_file_path, log_level=LEVELS.INFO, formatter=FORMATTERS.CLASSIC,
            dt_formatter=DT_FORMATTERS.CLASSIC)

    L = get_logger('nazwa', console_handler=ch, file_handler=fh)

    ...

    L.debug('debugowanie')
    L.info('informacja')
    L.warning('ostrzezenie')
    L.error('błąd')
"""

from .dvik_logging import get_logger
from .dvik_logging import get_console_handler, get_file_handler
from .dvik_logging import FORMATTERS, DT_FORMATTERS
