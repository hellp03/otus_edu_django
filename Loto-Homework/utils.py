import os

def clean_monitor():
    """Функция отчистки экрана."""
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')