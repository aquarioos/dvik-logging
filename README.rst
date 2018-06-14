dvik-logging
============

Pakiet umożliwiający pobranie obiektu *logging.Logger* podając nazwę i uchwyty do konsoli i pliku. W tym rozwiązaniu jest również sprawdzane, czy obiekt typu *Logger* o danej nazwie już istnieje. Jeśli tak, to nie jest tworzony nowy, lecz funkcja *get_logger* zwraca już istniejący obiekt typu *Logger*.

Użycie
------

.. code-block:: python
    :caption: Minimalna konfiguracja (z użyciem wartości domyślnych).

    import dvik_logging as dvl

    #
