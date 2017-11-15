.. _git_and_shyft:

***********************
Using Git for Shyft
***********************

Git is a version control tool that is becoming a standard in software development for:

* tracking changes over time in the source code
* facilitate parallel development between multiple model developers and research projects
* encourage peer code review and bug tracking, and
* to distribute official and bleeding edge releases of the model source code.


.. contents::
    :caption: Contents
    :local:
    :depth: 1



The following document is modified with attribute to the
`VIC developers <http://uw-hydro.github.io/>`_ who provided an original version of this
`Cookbook <https://github.com/UW-Hydro/VIC/wiki/Cookbook-for-Working-with-Git-and-VIC>`_.




Shyft for Model users (non developers)
========================================

In general, if you are only going to be using the model and not working
directly on the source code, it is best to follow the instructions: :ref:`user-install`.

Shyft for Developers
====================

If you plan on contributing to model development or would like a
systematic way to incorporate updates to the Shyft source code, we
encourage you to use Git. The following sections are designed to get you
started using git and working with the Shyft source code repository.

Git Resources
------------------

If you are not familiar with Git yet, we encourage you to spend a few
minutes getting antiquated with the system before you starting working
with the Shyft source code and Git. It's not difficult to use and a few
minutes of learning about Git will go along way in helping you manage
your code development.

There are a number of good Git learning resources that will provide a
basic introduction to the version control system.

* `Git SCM <http://git-scm.com/about>`_
* `Github <https://help.github.com/>`_


Getting the code
------------------
One could simply clone the shyft repository to get the code. However, we
prefer a few steps extra are taken to allow a better and more constructive
workflow following the standards of Git.

The basics steps to get the Shyft source code repository are described in
following (basically a Shyft specific rendition of
`fork-a-repo <https://help.github.com/articles/fork-a-repo>`_).


Step 0: A few definitions
++++++++++++++++++++++++++++

Using Git involves a few different copies of the archive:

1. **Truth Repo:** this is the master copy of the archive, maintained on
   the GitHub server by the Shyft Administrator.

2. **Your Fork of the Repo:** this is your version of the archive,
   maintained on the GitHub server by you. This is generally **not**
   where you edit code; it is more of a transfer point between your
   clone (see below) and the truth repo. Git keeps track of the
   differences between your fork and the truth repo. To move code
   changes from your fork to the truth repo, you must make a "pull
   request" for the Shyft administrator, who will do the actual pull.

3. **Your Clone(s) of your Fork:** a clone is a copy of your fork,
   stored on your local machine, where you can edit and test the code.
   You can have one or more clones. Each clone is a snapshot of a
   particular version of the code in your fork (e.g., you select which
   branches, and which versions of the code on those branches, to copy
   to your clone). You can change which version of the code each of your
   clones points to at any time. Your clone is where you edit files and
   commit changes. You can then push code changes from your clone back
   up to your fork.

Step 1: Fork the repositories
+++++++++++++++++++++++++++++

If you do not have a github account, create one. It's free for public
repos (like the Shyft one).

We develop Shyft using three different git repositories: the main software/code,
a second for test datasets, and a third repository for the documentation.

Go to the `statkraft <https://github.com/statkraft>`_ github page and for each
of the following repositories:

 * `statkraft/shyft <https://github.com/statkraft/shyft>`_
 * `statkraft/shyft-data <https://github.com/statkraft/shyft-data>`_
 * `statkraft/shyft-doc <https://github.com/statkraft/shyft-doc>`_

click "Fork" in the upper right hand corner.

Step 2: Clone your fork
++++++++++++++++++++++++

Now you've successfully forked the Shyft repositories, but so far they only exist
on GitHub. To be able to work on the project, you will need to clone them
to your local machine.

Shyft is distributed in three separate code repositories. The shyft repository
provides the main code base. A second repository (required for tests) is shyft-data.
A third repository shyft-doc is available containing example notebooks and tutorials.
The three repositories assume they have been checked out in parallel
into a shyft_workspace directory. The following commands in a bash shell should work.

.. code-block:: bash

    mkdir shyft_workspace && cd shyft_workspace
    export SHYFT_WORKSPACE=`pwd`
    git clone https://github.com/username/shyft.git
    git clone https://github.com/username/shyft-data.git
    git clone https://github.com/username/shyft-doc.git

This will create a directory ``shyft_workspace``, which we recommend using
as your main shyft development location. Then the commands create
clones of your fork of the repositories into the ``shyft_workspace``.

You are now ready to start working with the Python code base, but you still need
a binary of the C++ core if you don't wish to :ref:`dev-install`. Before we leave
the process of cloning the repositories, let's just take care of a few bookkeeping
items that will make life easier if you choose to develop and contribute code.

Step 3: Configure remotes
++++++++++++++++++++++++++++

When a repository is cloned, it has a default remote called ``origin``
that points to **your** fork on GitHub, **not** the original repository
it was forked from. To keep track of the original repository, you need
to add another remote. You can name this anything you want, but the name
``upstream`` is descriptive and an informal convention.

The following commands will make sure that you have your "upstream" remote
configured correctly by assigning the original repository to a remote tracking
branch called "upstream" for each of the repositories:

.. code-block:: bash

    cd shyft
    git remote add --tracking upstream https://github.com/statkraft/shyft.git
    cd ../shyft-data
    git remote add --tracking upstream https://github.com/statkraft/shyft-data.git
    cd ../shyft-doc
    git remote add --tracking upstream https://github.com/statkraft/shyft-doc.git
    cd $SHFYT_WORKSPACE

Now you have cloned all the repositories and configured remotes.

Step 4. Sync up your clone with the truth repo
+++++++++++++++++++++++++++++++++++++++++++++++

The following steps are something you'll want to do if you've forked and cloned
the code, but some time has passed, and you want to be sure you are working
on the most recent code.

4.a. Fetch information from the truth repo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now, Before starting to edit the code, pull in any new changes to the truth
repo that have been made by other people since you first created the
clone. You'll need to do this for each of the repositories you may be working
with.

.. code-block:: bash

    git fetch upstream

If you have already made changes to the code, this command by itself
will not overwrite your files. For updates from the truth repo to show
up in your files, you must do a **merge**.

4.b. Merge changes
~~~~~~~~~~~~~~~~~~

Determine which branches you will need to work with. At the very least,
this will include the master branch. If you are working on a hotfix or a
feature branch that already exists, you will need this branch as well;
the Shyft administrator has likely given you the name of the appropriate
branch to use. Alternatively, you may want to create a new branch (e.g.,
if you are the first person to work on a new feature or bug fix).

.. For
more information about the branches in the Shyft archive, see the `Shyft Git
Workflow Wiki <https://github.com/UW-Hydro/Shyft/wiki/Git-Workflow>`__.

For each branch, merge any changes from the truth repo into your local
version.

.. code-block:: bash

    git checkout branchname
    git merge upstream/branchname

where branchname = name of the branch


Next Steps
+++++++++++
At this point you have a complete clone of the shyft repositories in your
``shyft_workspace`` directory. You are ready to proceed to either build the
source code and C++ core, or you can download and install a binary of the api
and point your ``PYTHONPATH`` to it.





Working with the code
++++++++++++++++++++++

Making changes
~~~~~~~~~~~~~~

1. Select a branch
^^^^^^^^^^^^^^^^^^

Change your active branch to the desired branch.

.. code-block:: bash

    git checkout branchname

where "branchname" is the name of the branch

2. Make changes
^^^^^^^^^^^^^^^

You can edit the code using any editor or development environment you
prefer. You can also create new files, and move, rename, or delete
existing files. You will not be able to push these changes to your fork
until you **commit** them.

It is a good idea to **compile and test** your changes on your local
machine before you commit them. This avoids extra commits to fix typos,
etc.

At any point during the process of changing the code, you can pull in
any changes that other people have made via the fetch/merge procedure
described above.

Committing changes
~~~~~~~~~~~~~~~~~~

Before committing your changes, remove any extraneous files that have
been created during compiling and testing. Make sure you don't add temporary
files to your commit.

1. Register your changes for commit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To register the changes to (or creation of) a specific file::

    git add filename

To register moving or renaming any files::

    git mv oldpath/oldfilename newpath/newfilename

To register the deletion of a file::

    git rm filename

2. Commit the changes
~~~~~~~~~~~~~~~~~~~~~

The next step is to create a commit and commit message::

    git commit -m "your commit message"

The message should contain a description of the set of changes
(including a brief description of the problem that motivated the
changes). Save and exit.

Pushing commits to your fork
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After committing your changes, you should push them to your fork (which
has the alias ``origin``) stored on GitHub::

    git push origin branchname

where "branchname" is the name of the branch where you made the commits.

Making a pull request
~~~~~~~~~~~~~~~~~~~~~

To make your changes visible other users/developers, your changes must
be incorporated into the truth repo. To do this, you must create a pull
request on the GitHub server.

**NOTE:** We ask that you perform at least some basic tests on your code
before you issue a pull request. Make sure the code compiles and runs
for at least the test cases you have been working with. If it is a bug
fix, make sure that it actually fixes the bug. If possible, try to make
sure that it doesn't create a new bug. We are working on generating some
standard tests that everyone can download and run for this purpose;
until then, please test the code using your own input files.

The Shyft administrator and other developers will examine your pull
request and decide if/how they want to incorporate your changes into the
code.

Git Workflow
============

We have not yet implemented a Shyft-specific workflow. However, believe
the workflow developed by the VIC team provides a good resource at this time.
It requires developers to adhere to a few rules regarding branch names
and merge requests. A full description of the workflow can be found
`here <https://github.com/UW-Hydro/VIC/wiki/Git-Workflow>`__.
