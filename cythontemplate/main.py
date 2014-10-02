from cythontemplate.hellolib import hello
from cythontemplate.hellolib import cythonhello
from cythontemplate.hellolib.sublib import hello2
from cythontemplate.hellolib.sublib import cythonhello2


def main():
    hello.print_name()
    cythonhello.print_name()
    hello2.print_name()
    cythonhello2.print_name()


if __name__ == '__main__':
    main()
