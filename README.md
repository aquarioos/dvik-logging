# dvik-logging

Pakiet umożliwiający pobranie obiektu `logging.Logger` podając nazwę i uchwyty do konsoli i pliku. W tym rozwiązaniu jest również sprawdzane, czy obiekt typu `Logger` o danej nazwie już istnieje. Jeśli tak, to nie jest tworzony nowy, lecz funkcja `get_logger()` zwraca już istniejący obiekt typu `Logger`.

Kod był testowany dla Pythona 3.6.

## Instalacja

Najnowszą wersję paczki można pobrać z GitHuba.

`pip install git+https://github.com/aquarioos/dvik-logging/#egg=dvik-logging`

```
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

```
(venv) daniel@Vela ~ $ pip freeze
dvik-logging==0.2
(venv) daniel@Vela ~ $
```

## Formaty, poziomy logowania

Definiując `Logger` podaje się formaty logów i dat. W pakiecie są zdefiniowane gotowe formaty, które można użyć przy tworzeniu uchwytów. Są także przypisane wartości domyślne, dzięki czemu nie jest konieczne wybieranie formatów za każdym razem.

### Formaty linii

Formaty logowanych linii są wymienione w klasie `FORMATTERS`:

#### `FORMATTERS.CLASSIC`
```
2018-06-14 09:36:00 INFO     [nazwa] wiadomość
2018-06-14 09:36:22 WARNING  [nazwa] ostrzeżenie
2018-06-14 09:37:04 ERROR    [nazwa] błąd
```

#### `FORMATTERS.SHORT`
```
2018-06-14 09:36:00 INFO [nazwa] wiadomość
2018-06-14 09:36:22 WARNING [nazwa] ostrzeżenie
2018-06-14 09:37:04 ERROR [nazwa] błąd
```

#### `FORMATTERS.NO_TIME`
```
INFO     [nazwa] wiadomość
WARNING  [nazwa] ostrzeżenie
ERROR    [nazwa] błąd
```

### Formaty daty

Formaty dat są wymienione w klasie `DT_FORMATTERS`:

#### `DT_FORMATTER.CLASSIC`
```
2017-06-14 09:46:47
```

#### `DT_FORMATTER.TIME_FIST`
```
09:46:47 2017-06-14
```

#### `DT_FORMATTER.SHORT`
```
17-06-14 09:46:47
```

#### `DT_FORMATTER.TIME_ONLY`, `DT_FORMATTER.NO_DATE`
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

## Użycie

```python
import dvik_logging as dvl

# tworzymy uchwyt do konsoli
ch = dvl.get_console_handler()

# tworzymy uchwyt do pliku
fh = dvl.get_file_handler('/sciezka/do/plik.log')

# pobieramy logger
L = dvl.get_logger('nazwa-loggera', console_handler=ch, file_handler=fh)

# teraz możemy pisać logi do konsoli i do pliku plik.log
L.info('informacja')
L.debug('debugowanie')
L.warning('ostrzeżenie')
```
