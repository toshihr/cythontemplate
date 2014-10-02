# -*- coding: utf-8 -*-
try:
    from Cython.Build import cythonize
    EXIST_CYTHON = True
except ImportError:
    EXIST_CYTHON = False
# http://wiki.python.org/moin/PortingPythonToPy3k
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py
from setuptools import find_packages
from setuptools.extension import Extension
# if cx_Freeze is unnecessary, then the 'setup' module should be imported from setuptools
from cx_Freeze import setup, Executable
import sys
import os.path
import glob
from itertools import chain

version = '1.0.0'

# cx_Freeze
build_exe_options = {'packages': ['os'], 'excludes': ['tkinter']}
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'


def _make_extensions(ext_name_with_wildcard):
    ext = '.pyx' if EXIST_CYTHON else '.c'
    filenames = glob.glob(ext_name_with_wildcard.replace('.', os.path.sep) + ext)

    return [Extension(
        name=filename.replace(os.path.sep, '.')[:-len(ext)],
        sources=[filename],
        extra_compile_args=["-Wno-unneeded-internal-declaration", "-Wno-unused-function"],
    ) for filename in filenames]


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]


def _install_requires():
    return _load_requires_from_file('requirements.txt')


def _test_requires():
    return _load_requires_from_file('test-requirements.txt')


packages = find_packages(exclude=['tests'])

# gather package/*.[pyx|c]
extensions = list(chain.from_iterable(map(lambda s: _make_extensions(s + '.*'), packages)))

if EXIST_CYTHON:
    print('cythonizing...')
    extensions = cythonize(extensions)

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
    scripts=[],
    entry_points={'console_scripts': ['cythontemplate = cythontemplate.main:main']},
    cmdclass={'build_py': build_py},
    # cx_Freeze
    # options={'build_exe': build_exe_options},
    executables=[Executable('cythontemplate/main.py', base=base)],
)
