## Setting up your Shyft Environment

In order to run Shyft and use the notebooks tutorials, you will have to make sure your 
Shyft environment is correctly configured. This is detailed in the [Environment Variables](http://shyft.readthedocs.io/en/latest/installing.html#environment-variables) section of the installation 
instructions.

This step is highly specific on how and where you have installed Shyft. If you have followed the guidelines at github, and cloned the three shyft repositories: i) shyft, ii) shyft-data, and iii) shyft-doc, you may need to tell jupyter notebooks where to find shyft.

The code block below is included in most the notebooks, and is an example of how to be sure Shyft find
the data required for the tutorials.

If you have a 'system' shyft, or used `conda install -s sigbjorn shyft` to install shyft, then you probably will want to make sure you have set the SHYFT_DATA directory correctly, as otherwise, Shyft will assume the above structure and fail. __This has to be done _before_ `import shyft`__.

The most important point is that `SHYFT_DATA` points to the directory where you either have your data
to work with, or in the case of the tutorials, points where you have cloned the [shyft-data](https://github.com/statkraft/shyft-data) repository.

**note**: it is most likely that you'll need to do one or the other below:


    # try to auto-configure the path. This will work in the case
    # that you have checked out the doc and data repositories
    # at same level. Make sure this is doen **before** importing shyft
    shyft_data_path = path.abspath("../../../shyft-data")
    if path.exists(shyft_data_path) and 'SHYFT_DATA' not in os.environ:
        os.environ['SHYFT_DATA']=shyft_data_path
        
    # shyft should be available either by it's install in python
    # or by PYTHONPATH set by user prior to starting notebook.
    # This is equivalent to the two lines below
    #  shyft_path=path.abspath('../../../shyft')
    #  sys.path.insert(0,shyft_path)