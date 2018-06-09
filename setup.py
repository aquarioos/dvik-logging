from setuptools import setup

setup(
    name='dvik-logger',
    version='0.1',
    description='Pakiet pisany w ramach projektu DVik. Jest to dodatkowa warstwa na bibliotekę logging. Umożliwi łatwe pobranie i skonfigurowanie obiektu loggera wraz z odpowiednimi uchwytami (handlerami).',
    url='https://github.com/aquarioos/dvik-logging',
    author='Daniel Taranta',
    author_email='aquarioos@yandex.com',
    license='MIT',
    packages=['dvik_logging'],
    zip_safe=False
)