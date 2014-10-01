from hellolib import hello
from hellolib import cythonhello
from hellolib.sublib import hello2
from hellolib.sublib import cythonhello2

if __name__ == '__main__':
    hello.print_name()
    cythonhello.print_name()
    hello2.print_name()
    cythonhello2.print_name()
