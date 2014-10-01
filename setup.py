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
# http://wiki.python.org/moin/PortingPythonToPy3k
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py
from setuptools import setup, find_packages
from setuptools.extension import Extension
import os.path
import glob
from itertools import chain

version = '1.0.0'


def _make_extensions(ext_name_with_wildcard):
    ext = '.pyx' if USE_CYTHON else '.c'
    filenames = glob.glob(ext_name_with_wildcard.replace('.', os.path.sep) + ext)

    return [Extension(
        name=filename.replace(os.path.sep, '.')[:-len(ext)],
        sources=[filename],
        extra_compile_args=["-Wno-unneeded-internal-declaration", "-Wno-unused-function"],
    ) for filename in filenames]


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

# gather package/*.[pyx|c]
extensions = list(chain.from_iterable(map(lambda s: _make_extensions(s + '.*'), packages)))

_do_cythonize()

setup(
    name='cythontemplate',
    version=version,
    description='Cython + Nose project template',
    url='https://github.com/kerug/cythontemplate',
    long_description=open('README.rst').read() + '\n' + open('CHANGELOG.txt').read(),
    classifiers=['Topic :: Software Development :: Libraries :: Python Modules'],
    keywords='Cython Nose setup.py template',
    author='kerug',
    author_email='keru.work@gmail.com',
    license='Freeware',
    packages=packages,
    # package_data=, # works for bdist, not for sdist. MANIFET.in works in reverse
    install_requires=_install_requires(),
    tests_require=_test_requires(),
    test_suite='nose.collector',
    zip_safe=False,
    ext_modules=extensions,
    # scripts=[],
    entry_points={'console_scripts': ['cythontemplate = cythontemplate.main:main']},
    cmdclass={'build_py': build_py},
)
