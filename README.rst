.. image:: https://travis-ci.org/5j9/flake8-no-u-prefixed-strings.svg?branch=master
    :target: https://travis-ci.org/5j9/flake8-no-u-prefixed-strings

flake8-no-u-prefixed-strings
----------------------------
A plugin for flake8 (v3+) to disallow any u-prefixed string literals, e.g. ``u""``, ``u''``, ``U""""text"""``, or ``u'''string'''``.
Might be useful in Python 3 only projects, or Python 2 projects which enforce usage of ``unicode_literals``.

You can use `flake8-future-import <https://github.com/xZise/flake8-future-import>`_ to enforce import of ``unicode_literals``.

Installation
------------

.. code-block:: bash

  pip install flake8-no-u-prefixed-strings


Should work with all officially supported Python versions, including
Python 2.7.
