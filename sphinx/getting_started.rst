************************
Getting Started
************************
Shyft is meant to provide facilities for conducting hydrologic simulations and accessing uncertainty resulting from the forcing data and decisions regarding model structure.
It is a `framework <https://en.wikipedia.org/wiki/Software_framework>`_  which provides an `API <https://en.wikipedia.org/wiki/Application_programming_interface>`_. Shyft is written in `Python <https://python.org>`_ and `C++ <https://isocpp.org/>`_ using `Boost Python <http://boostorg.github.io/python/doc/html/index.html>`_ to enable interoperability.

As much of the core functionality is written in C++, there may be some caveats and paradigms that will be unfamiliar to pure python users. As such, a few key pieces of information are provided below that you should be aware of before working through the tutorials.

Tutorials and notebooks are provided as the main tool for introducing the different elements of the Shyft framework. These are under continuous development, and we seek user input. If you are interested to `contribute <https://github.com/statkraft/shyft-doc#contributing>`_ a notebook, please see the main `shyft-doc <https://github.com/statkraft/shyft-doc>`_ repository for instructions.

**IMPORTANT**: read and understand the following guidelines before working with the tutorials.

.. toctree::
   :glob:
   :maxdepth: 1

   help
   shyft_env

Notebook tutorials
========================

The best way to get started with Shyft is to work on some of the notebooks that we have developed.
To accomplish this it is recommended to checkout the `shyft-doc <https://github.com/statkraft/shyft-doc>`_ repository
and work using the `Jupyter <https://jupyter.org>`_ notebooks contained within the `notebooks` folder.

They are available here in static form:

.. toctree::
   :maxdepth: 2

   notebook
