.. _python-install:

****************************
Python Installation Guide
****************************

We provide our recommendation for installing Python. This is not a requirement, but a general recommendation
is to use conda from `Continuum Analytics <http://conda.pydata.org/docs/get-started.html>`_. Below are instructions
to create an Anaconda environment. Along with running Shyft, there are several other resources this
will provide for plotting and visualization of results -- including jupyter for running the tutorial notebooks.

.. note::

    If you prefer a leaner solution, simply use the requirements.txt file included with the repository and a miniconda environment.

Unless you are building from scratch using one of the provided build scripts or would prefer to use an
isolated miniconda environment for Shyft, we recommend (and only provide instructions for) setting up
a `conda environment <http://conda.pydata.org/docs/using/envs.html#create-an-environment>`_:

.. code-block:: bash

    conda create --name shyft python=3.6 anaconda


A few other customizations to the environment will help with your workflow. First, define
a few ``env_vars`` for the new environment. The easiest way to do this is to find the directory where
you've created your environment (if you followed above: ``$HOME/.conda/envs/shyft``). Inside that directory
create the following files:

.. code-block:: bash

    cd $HOME/.conda/envs/shyft
    mkdir -p ./etc/conda/activate.d
    mkdir -p ./etc/conda/deactivate.d
    touch ./etc/conda/activate.d/env_vars.sh
    touch ./etc/conda/deactivate.d/env_vars.sh


Then edit the ``$HOME/.conda/envs/shyft/etc/conda/activate.d/env_vars.sh`` file to include the following environment variables:

.. code-block:: bash

    #!/bin/bash
    SHYFT_WORKSPACE=/path/to_directory_into_which_you_cloned/shyft-repositories

    #SHYFT
    export SHYFT_DEPENDENCIES_DIR=$SHYFT_WORKSPACE/shyft-dependencies
    export LD_LIBRARY_PATH=$SHYFT_DEPENDENCIES_DIR/local/lib
    export PYTHONPATH=$SHYFT_WORKSPACE/shyft

Next edit the ``$HOME/.conda/envs/shyft/etc/conda/deactivate.d/env_vars.sh`` file to unset the environment variables:

.. code-block:: bash

    #!/bin/bash

    #SHYFT
    unset SHYFT_DEPENDENCIES_DIR
    unset PYTHONPATH

Now, to build activate the shyft environment and cd to your ``$SHYFT_WORKSPACE`` directory:

.. code-block:: bash

    bash
    source activate shyft
    cd $SHYFT_WORKSPACE/shyft

And you should be ready to start :ref:`user-install` or :ref:`contrib-install` of Shyft!
