from cythontemplate.hellolib import hello
from cythontemplate.hellolib import cythonhello


class TestAdd:

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_add(self):
        s = hello.add(1, 5)
        assert s == 6

    def test_cython_add(self):
        s = cythonhello.add(1, 5)
        assert s == 6
