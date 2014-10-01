cythontest: template for Cython + Nose project.
==================================

You should modify the following files based on your project:

- `setup.py`
- `MANIFEST.in`
- `requirements.txt`
- `test-requirements.txt`

## Development & Tests
### build

```sh
$ python setup.py develop
```

### test

```sh
$ python setup.py nosetests
```

### clean
```sh
$ python setup.py develop -u
$ python setup.py clean -all
```

## Packing the project
```sh
$ python setup.py sdist
```


## ISSUE
- Cythonがないときにbuildでエラーを起こす
- setup.py develop で pipがバグる -> pipのバグ

## TODO
- cx_freezeパッケージングに対応する
- ToxによるPython2,3環境でのテストに対応