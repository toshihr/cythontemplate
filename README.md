cythontemplate: template for Cython + Nose project.
==================================

You should modify the following files based on your project:

- `setup.py`
- `MANIFEST.in`
- `requirements.txt`
- `test-requirements.txt`

## Development & Tests
### Setup
You can use `pyenv` and `virtualenv`. Mac OS X users can install these tools via Homebrew.
```
$ brew install pyenv-virtualenv
```


```
$ cd <project dir>
$ pyenv install 2.7.8
$ pyenv virtualenv 2.7.8 env_python2
$ pyenv local env_python2
```
Then you should install dependencies.
```
$ pip install -r test-requirements.txt
$ pyenv rehash
```


### Build

```
$ python setup.py develop
```

### Test
```
$ python setup.py nosetests
```

### Clean
```
$ python setup.py develop -u
$ python setup.py clean -all
```

### Update dependencies
```
$ pip freeze > test-requirements.txt
```

## Packing the project
```sh
$ python setup.py sdist
```

## Install
```sh
$ python setup.py install
$ pyenv rehash
```

## Uninstall
```sh
$ pip uninstall cythontemplate
```

## CLI command
after install, you can use CLI command:
```sh
$ cythontemplate
```
