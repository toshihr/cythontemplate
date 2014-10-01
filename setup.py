# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
try:
    from future_builtins import map
except ImportError:
    # Python 3 raise ImportError
    pass
try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False
from setuptools import setup, find_packages
from setuptools.extension import Extension
import os.path


version = '1.0.0'


def _make_extension(ext_name):
    ext = '.pyx' if USE_CYTHON else '.c'
    filename = ext_name.replace('.', os.path.sep) + ext
    return Extension(
        ext_name,
        [filename],
        extra_compile_args=["-Wno-unneeded-internal-declaration", "-Wno-unused-function"],
    )


def _do_cythonize():
    if USE_CYTHON:
        global extensions
        print('cythonizing...')
        extensions = cythonize(extensions)


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]


def _install_requires():
    return _load_requires_from_file('requirements.txt')


def _test_requires():
    return _load_requires_from_file('test-requirements.txt')


packages = find_packages(exclude=['tests'])

# *.pyx or *.c
extensions = list(map(lambda s: _make_extension(s + '.*'), packages))

_do_cythonize()

setup(
    name='cythontemplate',
    version=version,
    description='cython + nose project template',
    # url='',
    # classifiers=,
    # keywords=,
    author='kerug',
    author_email='keru.work@gmail.com',
    license='MIT',
    packages=packages,
    # package_data=, # works for bdist, not for sdist. MANIFET.in works in reverse
    install_requires=_install_requires(),
    tests_require=_test_requires(),
    ext_modules=extensions,
    # scripts=[],
    # entry_points={'console_scripts': ['cythontemplate = cythontemplate:main']},
)
