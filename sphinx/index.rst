.. Shyft documentation master file, created by
   sphinx-quickstart on Thu Sep 24 19:06:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

************************************************************
Shyft: Statkraft's Hydrologic Forecasting Toolbox
************************************************************

Shyft is an Open Source modern computing framework for running spatially distributed conceptual hydrologic models. It allows for simulation of different algorithms in a highly efficient manner, while providing an interface to conduct more explorative evaluations of the hydrologic performance of the available algorithms. Shyft is not simply a model, nor is it a distinct "platform". The software provides a high level Python based interface to a modern, C++ based underlying API.

The objectives of Shyft are to:

- provide a flexible hydrologic forecasting toolbox built for operational environments
- enable highly efficient / rapid calculations of hydrologic response at the regional scale
- allow for using the multiple working hypothesis to obtain an optimal catchment forecast
- create a mechanism for rapid implementation of improvements identified through research activities


To address the first and second objectives, computational efficiency and well test-covered software have been paramount. Shyft is inspired from research software that provided for the multiple working hypothesis. Shyft uses the latest C++ standards to make use of templated code in order to provide highly efficient code taking advantage of modern day compiler functionality minimizing risk of faulty code and memory leaks. To address the latter two objectives, the templated language functionality allows for the development of different algorithms that are then easily implemented into the framework. The `api` allows for accessing all the components of the framework, including the individual hydrologic routines easily and is exposed to both the C++ and Python languages allowing for rapid exploration of different model configurations and selection of an optimal forecast model.

Documentation
==============

Documentation of Shyft is available at `shyft.readthedocs.io <https://shyft.readthedocs.io>`_ and is under continuous development.

Our primary source of documentation is through this website.


Contents:

.. toctree::
    :maxdepth: 2

    installing
    getting_started
    orchestration
    config_files


Indices and tables
-------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`