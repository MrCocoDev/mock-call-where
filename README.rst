.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/mock-call-where.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/mock-call-where
    .. image:: https://readthedocs.org/projects/mock-call-where/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://mock-call-where.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/mock-call-where/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/mock-call-where
    .. image:: https://img.shields.io/pypi/v/mock-call-where.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/mock-call-where/
    .. image:: https://img.shields.io/conda/vn/conda-forge/mock-call-where.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/mock-call-where
    .. image:: https://pepy.tech/badge/mock-call-where/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/mock-call-where
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/mock-call-where

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/
.. image:: https://img.shields.io/pypi/v/mock-call-where.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/mock-call-where/
.. image:: https://github.com/MrSage/mock-call-where/actions/workflows/ci.yml/badge.svg
    :alt: GitHub Test CI
    :target: https://github.com/MrSage/mock-call-where/actions/workflows/ci.yml
.. image:: https://pepy.tech/badge/mock-call-where/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/mock-call-where

|

===============
mock-call-where
===============


    A short little plugin to find where a mock was called!


How to Use
==========

This library is setup as a pytest plugin, so if you're using pytest you can just add
the `mock_where` fixture in your tests. If you'd like to always have it enabled...


Manually Enabling/Disabling
===========================

::

    from mock_call_where.override import AdvancedCall

    AdvancedCall.apply()
    ...  # The plugin is enabled now
    AdvancedCall.unapply()


.. _pyscaffold-notes:

Making Changes & Contributing
=============================

This project uses `pre-commit`_, please make sure to install it before making any
changes::

    pip install pre-commit
    cd mock-call-where
    pre-commit install

It is a good idea to update the hooks to the latest version::

    pre-commit autoupdate

Don't forget to tell your contributors to also install and use pre-commit.

.. _pre-commit: https://pre-commit.com/

Note
====

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.
