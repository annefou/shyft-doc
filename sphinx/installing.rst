************
Installation
************

There are several different methods to get up and running with Shyft depending on your intended use.
We categorize users into several categories:

- **users**: users who are interested in using Shyft for hydrologic analysis. First time users should probably start here to at least gain familiarity of the functionality of the framework.
- **contributers**: users who will explore the Python api and may contribute back to the project.
- **developers**: users who are interested in the C++ core, and are interested in creating their own algorithms. Advance programming skills and familiarity is required.

The reason to categorize users relates to the installation requirements. For both *users* and *contributers* it is not necessary to build/compile the C++ core, and one can simply use available distributions.

Shyft is developed for both Unix-like (*nix) and Windows operating systems, though our preference is linux.

.. contents::
   :local:
   :depth: 1


Minimum Requirements
=====================
Shyft is developed with Python and C++ coding standards. Our choice of Python is `Anaconda <https://www.anaconda.com>`_ and we recommend using the `conda <https://conda.io>`_ package management system. It is fine to use `Miniconda <https://conda.io/docs/glossary.html#miniconda-glossary>`_ if you don't want to install the full Anaconda Distribution.


* 64-bit computer.
* Windows or Linux.
    - `ms c++ vs 2017 redist <https://go.microsoft.com/fwlink/?LinkId=746572>`_ (if using Windows)
* C++11
* Python >= 3.5
* Python libraries:
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

NOTE: You do not need administrative or root permissions to
install Shyft if you select a user-writable install location.

Using a Conda channel
=====================

The simplest way to get started, if you are familiar with conda is to use Sigbjorn's channel:

    ``conda  create -c sigbjorn -c conda-forge -n shyft python=3.6 pyyaml numpy netcdf4 gdal matplotlib requests nose coverage pip shapely pyproj jupyter pandas shyft``

If you have some problems with dependencies you may need to follow one of the more detailed `Installation Recipes`_.

Installing from source
=====================

If you may be interested in modifying the Python code and contributing to the project, you will probably want to check out the repositories and install Shyft from source.

Clone the repositories
-----------------------

Shyft is distributed in three separate code repositories: The main code base `shyft <https://github.com/statkraft/shyft>`_. A second repository (required for tests) is located at `shyft-data <https://github.com/statkraft/shyft-data>`_. A third repository `shyft-doc <https://github.com/statkraft/shyft-doc>`_ is available containing example notebooks and tutorials. The three repositories assume they have been checked out in parallel into a ``shyft_workspace`` directory::

    bash
    mkdir shyft_workspace && cd shyft_workspace
    export SHYFT_WORKSPACE=`pwd`
    git clone https://github.com/statkraft/shyft.git
    git clone https://github.com/statkraft/shyft-data.git
    git clone https://github.com/statkraft/shyft-doc.git


Building with Cmake
--------------------

On many linux systems, it is easy to simply use our `cmake <https://cmake.org/>`_ approach. In order to do this, however, a few additional requirements must be fulfilled:

- A C++1y compiler (gcc-5 or higher)
- The BLAS and LAPACK libraries (development packages)
- A Python3 (3.4 or higher) interpreter
- The NumPy package (>= 1.8.0)
- The netCDF4 package (>= 1.2.1)
- The CMake building tool (2.8.7 or higher)

Once you've satisfied the above requirements you should be able to simply ``cd shyft`` into the Shyft repository and::

   $ python setup.py build_ext --inplace

This will call a script ``build_api_cmake.sh`` from the main `Shyft repository <https://github.com/statkraft/shyft>`_.

.. seealso:: If you have problems with dependencies, be sure to see the notes within the ``build_api.sh`` regarding the library paths.


Installation Recipes
=====================

If you are completely new to working with git repositories and building code, you do not need to compile the Shyft source, and we recommend one of the following recipes:


* :doc:`Conda Complete Recipe <recipe_conda-complete>`.





..
    .. doxygenindex::
      :outline:
    .. automodule:: shyft
      :members:

