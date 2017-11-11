************************
Getting Started
************************

Compiling
=====================

Instructions for building and compiling Shyft are available on the github wiki:

`Shyft Wiki <http://github.com/statkraft/shyft/wiki/>`_


Installing
=====================

Once you tested you Shyft package you can install it in your system via::

    $ python setup.py build_ext --inplace


Testing
=====================

The way to test Shyft is by running::

  $ nosetests

from the root directory (your will need the numpy and nose packages).

The test suite is not very comprehensive yet, but at least would provide indications that your installation is sane.

Running a small example
=====================

The best way to get started with Shyft is to work on some of the notebooks that we have developed.

.. toctree::
   :maxdepth: 2

   notebook
