def print_name():
    print(__name__)


def add(num1, num2):
    if (num1 is None):
        raise RuntimeError('num1 is None')
    return num1 + num2
