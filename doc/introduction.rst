What is Shyft?
===============

The Statkraft Hydrologic Forecasting Toolbox (Shyft), is OpenSource software developed to efficiently conduct hydrologic simulations in an operational environment. It allows for simulation of different algorithms in a highly efficient manner, while providing an interface to conduct more explorative evaluations of the hydrologic performance of the available algorithms. Shyft is not simply a model, nor is it a distinct "platform". The software provides a high level Python based interface to a modern, C++ based underlying API.

The development of Shyft was initially financed by Statkraft for the purpose of improving hydrological forecasting for hydropower scheduling. The aim of this development is to provide a framework that provides robust and tested code that may be used in operational environments, while engaging the scientific research community to work on a common hydrologic modeling platform. Shyft has a goal to provide numerous possible solutions for hydrologic simulation, and to provide a robust API to explore the various hydrologic routines.

Users may develop algorithms in either C++ or Python to test and explore their performance in a complete hydrologic simulation. Our primary source of documentation is through this website and on the `shyft wiki <https://github.com/statkraft/shyft/wiki>`_.

    

.. 
    .. doxygenindex::
      :outline:
    .. automodule:: shyft
      :members:

