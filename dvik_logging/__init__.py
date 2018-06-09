"""
DVikLogging
~~~~~~~~~~~~

Pakiet pisany w ramach projektu DVik. Jest to dodatkowa warstwa na bibliotekę logging. Umożliwi łatwe pobranie i skonfigurowanie obiektu loggera wraz z odpowiednimi uchwytami (handlerami).

Przykładowe użycia:

TODO
"""

from .dvik_logging import get_logger
from .dvik_logging import get_console_handler, get_file_handler
from .dvik_logging import FORMATTERS, DT_FORMATTERS
