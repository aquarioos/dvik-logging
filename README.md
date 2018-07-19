# dvik-logging

Pakiet umożliwiający pobranie obiektu `logging.Logger` podając nazwę i uchwyty do konsoli i pliku. W tym rozwiązaniu jest również sprawdzane, czy obiekt typu `Logger` o danej nazwie już istnieje. Jeśli tak, to nie jest tworzony nowy, lecz funkcja `get_logger()` zwraca już istniejący obiekt typu `Logger`.

Kod był testowany dla Pythona 3.6.

## Wersja

Aktualną wersją jest `1.0`. W tej wersji zostało zmienione API pakietu (aktualne opisane w rozdziale **Funkcje**).

## Instalacja

Najnowszą wersję paczki można pobrać z GitHuba.

`pip install git+https://github.com/aquarioos/dvik-logging/#egg=dvik-logging`

```sh
(venv) daniel@Vela ~ $ pip install git+https://github.com/aquarioos/dvik-logging/#egg=dvik-logging
Collecting dvik-logging from git+https://github.com/aquarioos/dvik-logging/#egg=dvik-logging
  Cloning https://github.com/aquarioos/dvik-logging/ to /private/var/folders/3h/hvkgh03x4wz5ygjn7dxyp3zw0000gn/T/pip-install-pp9_ydp0/dvik-logging
Building wheels for collected packages: dvik-logging
  Running setup.py bdist_wheel for dvik-logging ... done
  Stored in directory: /private/var/folders/3h/hvkgh03x4wz5ygjn7dxyp3zw0000gn/T/pip-ephem-wheel-cache-xhwipvn8/wheels/ad/f6/c1/f368716cfeeb1dbbc3c29863127e747f47326a498b7fb55501
Successfully built dvik-logging
Installing collected packages: dvik-logging
Successfully installed dvik-logging-0.2
(venv) daniel@Vela ~ $
```

Jeśli nie było żadnych błędów, to *dvik-logging* powinien znajdować się na naszej liście pakietów.

```sh
(venv) daniel@Vela ~ $ pip freeze
dvik-logging==0.2
(venv) daniel@Vela ~ $
```

## Funkcje

`add_file_handler(logger_name, file_path, log_level='info', line_format='classic', dt_format='classic')`

    Dodaje do loggera o podanej nazwie uchwyt do pliku o podanych parametrach.

    Args:
        logger_name (str): nazwa loggera
        file_path (str): ścieżka do pliku logów
        log_level (str, optional): poziom logowania, domyślnie "info"
        line_formatter (str, optional): format logowanej linii, domyślnie "classic"
        dt_formatter (str, optional): format logowanej daty, domyślnie "classic"

    Raises:
        ValueError: jeśli nie ma loggera o podanej nazwie lub parametr słownikowy jest niepoprawny

`add_console_handler(logger_name, log_level='debug', line_format='classic', dt_format='classic')`

    Dodaje do loggera o podanej nazwie uchwyt do konsoli o podanych parametrach.

    Args:
        logger_name (str): nazwa loggera
        log_level (str, optional): poziom logowania, domyślnie "debug"
        line_formatter (str, optional): format logowanej linii, domyślnie "classic"
        dt_formatter (str, optional): format logowanej daty, domyślnie "classic"

    Raises:
        ValueError: jeśli nie ma loggera o podanej nazwie lub parametr słownikowy jest niepoprawny

`clear_handlers(logger_name)`

    Czyści uchwyty (handlery) w loggerze o podanej nazwie.

    Args:
        logger_name (str): nazwa loggera, w którym mają być wyczyszczone uchwyty (handlery)

    Raises:
        ValueError: jeśli logger o podanej nazwie nie istnieje

`create_logger(logger_name)`

    Tworzy logger o podanej nazwie (jeśli nie istnieje).

    Args:
        logger_name (str): nazwa loggera

    Returns:
        logging.Logger: utworzony logger

`get_logger(logger_name, ch_params=None, fh_params=None)`

    Pobiera logger. Jeśli logger o podanej nazwie już istnieje, to zwraca istniejący.

    Args:
        logger_name (str): nazwa loggera
        ch_params (dict): słownik z parametrami console handlera
        fh_params (dict): słownik z parametrami file handlera

    Returns:
        logging.Logger: obiekt loggera

    Raises:
        KeyError: jeśli nie podano ścieżki do pliku logów

## Formaty, poziomy logowania

Definiując `Logger` podaje się formaty linii i daty. W pakiecie są zdefiniowane gotowe formaty, które można użyć przy tworzeniu uchwytów. Są także przypisane wartości domyślne, dzięki czemu nie jest konieczne wybieranie formatów za każdym razem.

### Formaty linii

#### `classic` (domyślnie)
```
2018-06-14 09:36:00 INFO     [nazwa] wiadomość
2018-06-14 09:36:22 WARNING  [nazwa] ostrzeżenie
2018-06-14 09:37:04 ERROR    [nazwa] błąd
```

#### `short`
```
2018-06-14 09:36:00 INFO [nazwa] wiadomość
2018-06-14 09:36:22 WARNING [nazwa] ostrzeżenie
2018-06-14 09:37:04 ERROR [nazwa] błąd
```

#### `no_time`
```
INFO     [nazwa] wiadomość
WARNING  [nazwa] ostrzeżenie
ERROR    [nazwa] błąd
```

### Formaty daty

#### `classic` (domyślnie)
```
2017-06-14 09:46:47
```

#### `time_first`
```
09:46:47 2017-06-14
```

#### `short`
```
17-06-14 09:46:47
```

#### `time_only`, `no_date`
```
09:46:47
```

### Poziomy logowania

Poziomy logowania odpowiadają poziomom w bibliotece `logging`.

`LEVELS.DEBUG`

`LEVELS.INFO`

`LEVELS.WARNING`

`LEVELS.ERROR`

`LEVELS.FATAL`

`LEVELS.CRITICAL`

<!--## Użycie-->

<!--```python-->
<!--import dvik_logging as dvl-->

<!--# tworzymy uchwyt do konsoli-->
<!--ch = dvl.get_console_handler()-->

<!--# tworzymy uchwyt do pliku-->
<!--fh = dvl.get_file_handler('/sciezka/do/plik.log')-->

<!--# pobieramy logger-->
<!--L = dvl.get_logger('nazwa-loggera', console_handler=ch, file_handler=fh)-->

<!--# teraz możemy pisać logi do konsoli i do pliku plik.log-->
<!--L.info('informacja')-->
<!--L.debug('debugowanie')-->
<!--L.warning('ostrzeżenie')-->
<!--```-->
