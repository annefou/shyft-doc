************************
Using a Conda channel
************************

The following page documents setting up Shyft from start to finish using conda channels.

In the platform specific subsections you find how to install the standard Python environment needed to run SHyFT.

A pre-built shyft-distro is available on anaconda channel sigbjorn, https://anaconda.org/sigbjorn, and the steps below describes how to get up and running.

Windows 7, 8, 10 (x64)
=======================

This recipe takes about 15-30 minutes to complete if everything flows ok.

.. hint:: For those working behind company firewalls, there might be download-issues. A possible `solution is here <http://seanlaw.github.io/2015/12/23/fetching-conda-packages-behind-a-firewall/>`_

1. Install git

   source: https://git-scm.com/download

   Optional info and more readings (not needed initially for install of
   shyft doc & demos)

   -  https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
   -  https://www.youtube.com/watch?v=HVsySz-h9r4

2. Copy/clone the needed shyft-doc and shyft-data for demo and learning

    We do this in git-bash, you will find this on the command menu after
    install git.

    Usually it is installed into::

        "C:\Program Files\Git\git-bash.exe"


    create `"C:\\workspace\\shyft"` or similar as workspace, in git bash shell::

        bash
        mkdir /c/workspace/shyft
        cd /c/workspace/shyft
        git clone https://github.com/statkraft/shyft-data
        git clone https://github.com/statkraft/shyft-doc

3. Install ms c++ vs 2017 redist runtime needed for shyft

    source: https://go.microsoft.com/fwlink/?LinkId=746572

4. Install miniconda

    source: https://conda.io/miniconda.html

    select 64 bit installer (windows), download and execute.

    install to standard location (e.g.: C::raw-latex:`\Miniconda`3)

    more info on conda:

    -  short: https://conda.io/docs/commands.html#conda-environment-commands
    -  complete: https://conda.io/docs/user-guide/index.html

5. Create and install shyft environment

    start cmd-window (Win-R:cmd )::

        cmd C:\Miniconda3\Scripts\activate
        conda create -c sigbjorn -c conda-forge -n shyft python=3.6 pyyaml numpy netcdf4 gdal matplotlib requests nose coverage pip shapely pyproj jupyter pandas shyft

6. Use the newly created shyft -environment

    start cmd-window (Win-R:cmd)::

        cmd C:\Miniconda3\Scripts\activate shyft
        set SHYFTDATA=C:\workspace\shyft
        cd C:\workspace\shyft\shyft-doc
        jupyter notebook

7. Developing and Scripting with shyft We strongly recommend using
   pycharm for this.

    source: https://www.jetbrains.com/pycharm/download/?fromIDE=#section=windows

    The open-source free community version is Ok.


Ubuntu 15.10 (x64)
=====================

Preconditions for doing this is that you have an update Ubuntu 15.10
(x64) distro with a local user, having internet access so that the
remaining component can be installed.

The recipies does not require you to have root-access or admin
privilegies, so you should be able to run the software on your local
user account.

shyft\_ws.sh: Script to establish a complete pre-built **s**\ hyft **w**\ ork\ **s**\ pace ~/sws
----------------------------------------------------------------------------------------------------

::

    #!/bin/bash
    #
    # Pre conditions:
    # sudo apt-get install git libblas-dev liblapack-dev
    # To use pycharm you also need java
    # sudo apt-get install openjdk-7-jre
    #
    echo SHyFT installer for Ubuntu 15.10
    echo
    echo Notice that you need to have installed git, blas and lapack
    echo the command is
    echo 'sudo apt-get install git libblas-dev liblapack-dev'
    echo
    export WORKSPACE=~/sws
    mkdir -p $WORKSPACE
    echo Creating initial shyft_workspace at $WORKSPACE
    unset PYTHONPATH
    cd $WORKSPACE

    if [ -d shyft ]; then
        # if we would like a floating distro, to like this
        pushd shyft
        git pull
        popd
    else
        git clone https://github.com/statkraft/shyft
    fi;

    if [ -d shyft-data ]; then
        pushd shyft-data
        git pull
        popd
    else
        git clone https://github.com/statkraft/shyft-data
    fi;
    #works for Ubuntu 15.10, given that you have blas+lapack
    echo Unzip latest distro for Ubuntu 15.10 into shyft
    tar -xf shyft-data/distro/SK_2016_03_18_Ubuntu_15_10_np110py35.tar.gz

    if [ ! -d miniconda ]; then
        if [ ! -f miniconda.sh ]; then
            wget  -O miniconda.sh http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
        fi;
        bash miniconda.sh -b -p $WORKSPACE/miniconda
        export PATH="$WORKSPACE/miniconda/bin:$PATH"
        conda config --set always_yes yes --set changeps1 no
        conda update conda
        conda create -n shyft_env pyyaml numpy libgfortran netcdf4 gdal matplotlib requests nose coverage pip shapely pyproj
    fi;
    echo .
    echo Done!

shyft\_env.sh: Script to enable the shyft workspace
-------------------------------------------------------

The script below should be executed to enable the above established
workspace. You can source the script (source ./shyft\_env.sh)

::

    #!/bin/bash
    export WORKSPACE=~/sws
    export PATH="$WORKSPACE/miniconda/bin:$PATH"
    source activate shyft_env
    export PYTHONPATH=$WORKSPACE/shyft
    echo LD_PRELOAD workaround for anaconda/ubuntu problem and GFORTRAN_4 problem applied
    export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libgfortran.so.3.0.0:/usr/lib/x86_64-linux-gnu/libgfortran.so.3
    echo Ready for shyft-work

Troubleshoothing
================

The following sections describes problems and solutions that we
currently know.

Ubuntu/Anaconda libgfortran GFORTAN\_4 not found
--------------------------------------------------

As of 2016.03.08, the latest Anaconda distro seems to have it's own
libgfortran, one step ahead of system libs.

A workaround found to work is to enforce use of the system libgfortran
instead of the one in the anaconda distro. You can enforce this, if you
execute this in the shell prior to running anaconda/shyft applications.

``export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libgfortran.so.3.0.0:/usr/lib/x86_64-linux-gnu/libgfortran.so.3``
