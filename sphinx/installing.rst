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

If you may be interested in modifying the Python code and contributing to the project, you will probably want to check out the repositories and install Shyft from source. Documentation for this is currently available at the Shyft repository. Follow the `Developer Documentation <https://github.com/statkraft/shyft#developer-documentation>`_.


Installation Recipes
=====================

If you are completely new to working with git repositories and building code, you do not need to compile the Shyft source, and we recommend one of the following recipes:


* :doc:`Conda Complete Recipe <recipe_conda-complete>`.





..
    .. doxygenindex::
      :outline:
    .. automodule:: shyft
      :members:

