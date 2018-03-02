************
Installation
************

There are several different methods to get up and running with Shyft depending on your
intended use.
We categorize users into several categories:

- **users** are those interested in using Shyft for hydrologic analysis. First time users should probably start with :ref:`user-install` to at least gain familiarity of the functionality of the framework.
- **contributers** are those who will explore the Python api and may contribute back to the project. You may want to modify Python source code, so you should follow the :ref:`contrib-install`.
- **developers** are those who are interested in the C++ core, and are interested in creating their own algorithms. Advance programming skills and familiarity is required. Developers will want to see both the :ref:`contrib-install` and :ref:`dev-install` documentation.

The reason to categorize users relates to the installation requirements. For **users**
it is not necessary to build/compile the C++ core, and one can simply use available
distributions. **Contributors** also don't need to build the C++ core, but will want
to clone the repository to have access to the Python source code -- mostly for making
modifications to orchestration.

Shyft is developed for both Unix-like and Windows operating systems, though we
have a strong preference for linux.


.. contents:: Contents
    :local:
    :depth: 1




System Requirements
=====================
Shyft is developed with Python and C++. Our choice of Python is
`Anaconda <https://www.anaconda.com>`_ and we recommend using the `conda <https://conda.io>`_
package management system. It is fine to use
`Miniconda <https://conda.io/docs/glossary.html#miniconda-glossary>`_ if you don't
want to install the full Anaconda Distribution. You can follow our :ref:`python-install` for Shyft.


.. env-vars:

Environment Variables
-----------------------

There are a few environment variables we use with Shyft. If you do not plan to do a :ref:`contrib-install` of Shyft,
these are not strictly required. If you know what you are doing, you can modify these to your
liking, but this is our recommendation:

``SHYFT_WORKSPACE``
    The main folder where you will in parallel clone the repositories and setup Shyft. You don't need
    to work here, but you will at likely point your ``PYTHONPATH`` here, along with some other runtime variables.
    You should use this as your main build directory.

``SHYFT_DEPENDENCIES_DIR``
    Optional, only if you know what you are doing, and would have a different working tree strucutre than the
    recommented relative-path oriented standard approach. :ref:`dev-install` for Shyft.

``SHYFT_DATA``
    If you install prebuilt shyft, conda install -c sigbjorn shyft, -then you
    need to set this variable to run the demo-notebooks that resides in the shyft-doc/notebooks directory.
    It should point to the `shyft-data <https://github.com/statraft/shyft-data>`_
    repository in order to run the tests. Default values  in the shyft code uses the shyft-data directory parallel
    to the shyft source code directory.

.. _run-dependencies:

Minimal 'Run' Requirements
---------------------------
If you are not planning on building Shyft, then the requirements are:

- 64-bit computer.
- Windows or Linux.
    - Windows: `ms c++ vs 2017 redist <https://go.microsoft.com/fwlink/?LinkId=746572>`_.
    - Linux: gcc-7 runtime libraries (e.g. libgcc)
- Python >= 3.6
- Python libraries:
    - pyyaml
    - numpy=1.13
    - netcdf4
    - gdal
    - matplotlib
    - requests
    - nose
    - coverage
    - pip
    - shapely
    - pyproj
    - jupyter
    - pandas

NOTE: You do not need administrative or root permissions to install Shyft if you select a
user-writable install location.

.. _build-requirements:

Build Requirements
--------------------

Significantly greater requirements exist if you intend to build the C++ core of Shyft.
In addition to the :ref:`run-dependencies` there are some basic requirements which we
leave to the user to be sure are met, as these are quite typical:

* A C++11 compiler (gcc-6 or higher)
* The BLAS and LAPACK libraries (development packages)
* A Python 3 (3.6 or higher) interpreter
* The NumPy package (>= 1.8.0)
* The netCDF4 package (>= 1.2.1)
* The CMake building tool (3.4 or higher)

In addition, a series of Python packages are needed mainly for running the tests. These
can be easily installed via::

    bash
    $ pip install -r requirements.txt

or, if you are using conda (see below)::

    bash
    $ cat requirements.txt | xargs conda install

This should provide you with everything required from Python.

.. _build-dependencies:

External Libraries
-------------------

The Shyft C++ core utilizes several modern frameworks including: `dlib <http://dlib.net/>`_,
`boost <http://www.boost.org/>`_, and `armadillo <http://arma.sourceforge.net/>`_. Lastly,
you need to be sure you have installed the ``python-dev`` package and ``locate Python.h``
returns the header file. If not, you'll need to be sure to point the ``LD_LIBRARY_PATH``
set correctly.

Notice that the shyft/build_support/build_dependencies.sh provides a one-liner complete setup,
including miniconda/python, dependencies build etc.

Instructions on building these are provided in :ref:`dev-install`.

.. _user-install:

Binary installation with the sigbjorn conda channel
=====================================================

If are not yet familiar with Python, we recommend seeing the :ref:`python-install` documentation.
The simplest way to get started, if you are familiar with conda is to use Sigbjorn's channel::

    conda  create -c sigbjorn -c conda-forge -n shyft python=3.6 pyyaml numpy=1.13 netcdf4 gdal matplotlib requests nose coverage pip shapely pyproj jupyter pandas shyft scipy

.. _releases:

Accessing pre-built binary releases
-------------------------------------

Ref to the anaconda.org/sigbjorn channel for prebuilt windows and linxu packages.

.. _contrib-install:

Source Installation
===============================

If you are interested in modifying the source code and contributing to the project, you
will probably want to check out the repositories and install Shyft from source, in which
case you'll need to clone or fork the repository. If you are serious about participating
in development, then it is best to fork the repo on github and start editing your own copy.

You are not able to push to the main Shyft repository directly. We follow a standard Git
workflow. For more information about working with the Shyft source code, please see the
following documents:

.. toctree::
    :maxdepth: 1

    git_and_shyft
    install_python

Once you are comfortable with your git configuration and python installation, the next steps
        are to follow the :ref:`dev-install`.

.. seealso::
    For **Contributers** it is important to note in the :ref:`dev-install` that we have
    a trick we use for those who don't want to build
    the dependencies and C++ core.


.. _dev-install:

Build Instructions
===============================

.. warning::

    This portion of the documentation is rapidly changing. We are migrating documentation from github to
    these pages.

Developers will also do a :ref:`contrib-install`. However, once you have cloned the repositories, you'll have extra steps
to be sure you have all the :ref:`build-requirements` in place and are able to build the :ref:`build-dependencies`
before building the C++ core itself. Documentation for this is currently available at the Shyft repository. Follow the
`Developer Documentation <https://github.com/statkraft/shyft#developer-documentation>`_.

.. contrib-trick:

A hack for contributers
------------------------

We are currently working on a more elegant solution, but for the moment, for those who wish to work with the
Python source code, but do not wish to `build` Shyft, we recommend simply installing the binaries, and then copying
the appropriate binary files (e.g. ``.so`` or ``.pyd`` files) into the appropriate shyft path within the repository.
Make sure you `PYTHONPATH` is pointing to the repository.



.. _install-recipes:

Installation Recipes
=====================

.. warning::

    The following may not be up to date

A few installation recipes for specific platforms exist:

* :doc:`Conda Complete Recipe <recipe_conda-complete>`.

* `Build C++ page on the wiki <https://github.com/statkraft/shyft/wiki/BuildCplusplus>`_.




