************
Installation
************

There are several different methods to get up and running with Shyft depending on your intended use.
We categorize users into several categories:

- **users** are those interested in using Shyft for hydrologic analysis. First time users should probably start with `Using a Conda channel to install a pre-built binary`_ to at least gain familiarity of the functionality of the framework.
- **contributers** are those who will explore the Python api and may contribute back to the project. If you want to modify Python source code, then you will have to `Install from source`_, but not necessarily `Build from source`_.
- **developers** are those who are interested in the C++ core, and are interested in creating their own algorithms. Advance programming skills and familiarity is required. Developers will want to `Build from source`_.

The reason to categorize users relates to the installation requirements. For **users** it is not necessary to build/compile the C++ core, and one can simply use available distributions. **contributors** also don't need to build the C++ core, but will want to clone the repository to have access to the Python source code -- mostly for making modifications to orchestration.

Shyft is developed for both Unix-like (*nix) and Windows operating systems, though we have a strong preference for linux.

.. contents::
   :local:
   :depth: 1


System Requirements
=====================
Shyft is developed with Python and C++. Our choice of Python is `Anaconda <https://www.anaconda.com>`_ and we recommend using the `conda <https://conda.io>`_ package management system. It is fine to use `Miniconda <https://conda.io/docs/glossary.html#miniconda-glossary>`_ if you don't want to install the full Anaconda Distribution.

Minimal Requirements
---------------------
If you are not planning on building Shyft, then the requirements are simply:

- 64-bit computer.
- Windows or Linux.
    - `ms c++ vs 2017 redist <https://go.microsoft.com/fwlink/?LinkId=746572>`_ (if using Windows)
- Python >= 3.5
- Python libraries:
    - pyyaml
    - numpy
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

NOTE: You do not need administrative or root permissions to install Shyft if you select a user-writable install location.

Build Requirements
--------------------
Significantly greater requirements exist if you intend to build the C++ core of Shyft. In addition to the `Minimal Requirements`_ there are some basic requirements which we leave to the user to be sure are met, as these are quite typical:

* A C++11 compiler (gcc-6 or higher)
* The BLAS and LAPACK libraries (development packages)
* A Python 3 (3.5 or higher) interpreter
* The NumPy package (>= 1.8.0)
* The netCDF4 package (>= 1.2.1)
* The CMake building tool (2.8.7 or higher)

In addition, a series of Python packages are needed mainly for running the tests. These can be easily installed via::

    bash
    $ pip install -r requirements.txt

or, if you are using conda (see below)::

    bash
    $ cat requirements.txt | xargs conda install

The Shyft C++ core utilizes several modern frameworks including: `dlib <http://dlib.net/>`_, `boost <http://www.boost.org/>`_, and `armadillo <http://arma.sourceforge.net/>`_. Lastly, you need to be sure you have installed the ``python-dev`` package and ``locate Python.h`` returns the header file. If not, you'll need to be sure to point the ``LD_LIBRARY_PATH`` set correctly.

Instructions on building these are provided in `Build from source`_.

.. _conda-channel:
Using a Conda channel to install a pre-built binary
=====================================================

The simplest way to get started, if you are familiar with conda is to use Sigbjorn's channel::

    conda  create -c sigbjorn -c conda-forge -n shyft python=3.6 pyyaml numpy netcdf4 gdal matplotlib requests nose coverage pip shapely pyproj jupyter pandas shyft

If you have some problems with dependencies you may try to install the `latest release <https://github.com/statkraft/shyft/releases>`_ or to follow one of the more detailed `Installation Recipes`_.



.. _install-source:
Install from source
=====================

If you are interested in modifying the Python code and contributing to the project, you will probably want to check out the repositories and install Shyft from source, in which case you'll need to clone or fork the repository. If you are serious about participating in development, then it is best to fork the repo on github and start editing your own copy.

You are not able to push to the main Shyft repository directly. We follow a standard Git workflow. For more information about working with the Shyft source code, please see the following documents:

.. toctree::
    :maxdepth: 1

    git_and_shyft


.. Documentation for this is currently available at the Shyft repository. Follow the `Developer Documentation <https://github.com/statkraft/shyft#developer-documentation>`_.


.. _build-source:
Build from source
===================



Installation Recipes
=====================

If you are completely new to working with git repositories and building code, you do not need to compile the Shyft source, and we recommend one of the following recipes:


* :doc:`Conda Complete Recipe <recipe_conda-complete>`.





