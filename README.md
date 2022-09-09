Flake8 JUnit asserts plugin
===========================

Check for JUnit assert statements in your tests.

This module provides a plugin for ``flake8``, the Python code checker.


Installation
------------

You can install or upgrade ``flake8-junit`` with these commands::

  $ pip install flake8-junit
  $ pip install --upgrade flake8-junit


Plugin for Flake8
-----------------

When both ``flake8`` and ``flake8-junit`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    5.0.4 (flake8-junit: 0.1.0, mccabe: 0.7.0, pycodestyle: 2.9.1, pyflakes: 2.5.0) CPython 3.9.9 on Darwin

Flake8 allows disabling some tests based on the folder:

```
[flake8]
per-file-ignores =
    tests/accounting/*: J10
```

Error codes
-----------

| Error Code  | Description                          |
| ----------- | ------------------------------------ |
| J100        | JUnit assert found                   |


Changes
-------

##### 0.1.1 - 2022-09-09

* First public release
