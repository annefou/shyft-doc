README
======

Shyft is an OpenSource hydrological toolbox developed by
[Statkraft](http://www.statkraft.com).

This repository contains the documentation for
[Shyft](https://github.com/statkraft/shyft). Currently two documentation
platforms are being used: 

* [doxygen](http://www.stack.nl/~dimitri/doxygen/) for the C++ code
* [sphinx](http://www.sphinx-doc.org) for the Python code

If you are reading this page, it assumes you are interested in contributing to the Shyft documentation. If you are looking **for the Shyft documentation**, the please see here:

[Shyft Documentation](http://shyft.readthedocs.io/)

Click the badge below to try out our Shyft jupyter dashboards:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/annefou/shyft-doc/master)


CONTRIBUTING
============

Contributions to the documenation are *strongly* welcomed. The easiest place to
start is through the notebooks. We love receiving jupyter notebooks with
examples!

As with the code base, to contribute to the documentation, we follow the
standard git clone --> pull request workflow.

CLONING
=========
As with the main [Shyft](https://github.com/statkraft/shyft) codebase, you should clone all three repositories to work with the documentation. Shyft is distributed in three separate code repositories. This repository, `shyft` provides the main code base. A second repository (required for tests) is located at [shyft-data](https://github.com/statkraft/shyft-data). A third repository [shyft-doc](https://github.com/statkraft/shyft-doc) is available containing example notebooks and tutorials. The three repositories assume they have been checked out in parallel into a `shyft_workspace` directory:

```bash
mkdir shyft_workspace && cd shyft_workspace
export SHYFT_WORKSPACE=`pwd`
git clone https://github.com/statkraft/shyft.git
git clone https://github.com/statkraft/shyft-data.git
git clone https://github.com/statkraft/shyft-doc.git
```

REQUIREMENTS
============

You should probably have a working Shyft build and a conda env, "shyft" for
example. See the [README](https://github.com/statkraft/shyft/#python-set-up) for more information. To contribute to the sphinx documention you will need the following sphinx extensions installed:

```bash
pip install breathe
pip install nbsphinx
```

You can just use: `conda env create --name shyft-doc --file sphinx/environment.yml`, if you like.


BUILDING SPHINX
================

If you have the sphinx and the extensions properly installed on your system, you should be able to run:

```bash
cd sphinx
make html
```

This will generate output in the `docs` directory.

Note that in `conf.py` there are settings controlling whether or not the notebooks will be built with the sphinx-build run. We have this set to off by default (the notebooks are not built on the readthedocs server). So, if you have create a new notebook, be sure to run all the code and save it with the output. Then sphinx-build will pick up the notebook in the state it was saved.

BUILDING DOXYGEN
================

To build the doxygen output:

```bash
cd doxygen
doxygen doxyconfig.core.conf 
```

Output is generated at: `core/html` and `core/xml`.

CONTRIBUTE A NOTEBOOK
======================

We love getting notebooks from users! If you have made a nice notebook demonstrating some functionality of Shyft you would like to share, it is easy to contribute. Simply clone the `shyft-doc` and `shyft-data` repositories, as instructed above. Then follow these instructions.

1. First add your data to the `shyft-data` repository:

```bash
cd shyft-data/contrib
git checkout -b my-example-data
mkdir my-example-data
cp -r ../your_data_source my-example-data
git add my-example-data/*
git commit -m "pushing data for my-example notebook"
```

2. Now change to the `shyft-doc` directory:

```bash
cd shyft-doc/contrib
git checkout -b my-example
git cp /path/to/yournotebook.ipynb .
git add yournotebook.ipynb
git commit -m "adding my super cool notebook"
```

Then create pull requests on github for your branches.



AUTHORS
=======

Documentation and Notebooks:
Sigbjørn Helset <Sigbjorn.Helset@statkraft.com>, Yisak Sultan Abdella <YisakSultan.Abdella@statkraft.com>, and John F. Burkhart <john.burkhart@statkraft.com>

THANKS
======

Contributors and current project participants include:
 * Sigbjørn Helset <Sigbjorn.Helset@statkraft.com>
 * Ola Skavhaug <ola@xal.no>
 * John Burkhart <John.Burkhart@statkraft.com>
 * Felix Matt <f.n.matt@geo.uio.no>
 * Francesc Alted <faltet@gmail.com>



COPYING / LICENSE
=================
Shyft is released under LGPL V.3
See LICENCE
