import os

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


install_and_import('boto3')
install_and_import('picamera')
install_and_import('time')
install_and_import('boto3')
install_and_import('RPi.GPIO')