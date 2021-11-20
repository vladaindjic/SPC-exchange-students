

# Software Patterns and Components

This repository contains materials and guidelines for the Software Patterns and Components course.
The goal of this course is to teach students how to develop software components in Python.
The reminder of the document assumes that you are using Linux operating system.
For other operating systems, you should consult the official documentation or [google.com](https://www.google.com/).


# Python Programming Languages

The programming language used for this course is [Python](https://en.wikipedia.org/wiki/Python_(programming_language)). The installation instructions can be found
at the [official documentation](https://www.python.org/). Note that the majority of Linux distributions already have preinstall
Python interpreter.

If you are not familiar with Python, it is recommended to do some Python
tutorials that can be easily found [on the web](https://www.youtube.com/results?search_query=python+tutorial).


## Python Tools

It is not recommended to use system interpreter while developing the application in Python.
Instead, the good practice is to use virtual environments.
This is what official documentations says about virtual environments:
/"A virtual environment is a Python environment such that the Python interpreter, libraries and scripts
installed into it are isolated from those installed in other virtual environments, and (by default) any
libraries installed in a “system” Python, i.e., one which is installed as part of your operating system.
A virtual environment is a directory tree which contains Python executable files and other files which
indicate that it is a virtual environment."/

To simplify, virtual environment contains the copy of system interpreter which should used
while developing Python applications without concerns that any important system library might get corrupted.   


### venv and virtualenv

[*venv*](https://docs.python.org/3/library/venv.html) and [*virtualenv*](https://virtualenv.pypa.io/en/latest/) could be used for maintaining virtual environments. From the user perspective,
both tools are equivalent. The *venv* should come preinstalled with newer versions of Python 3 interpreters,
while virtualenv requires [manual installation](https://virtualenv.pypa.io/en/latest/installation.html#via-pip).

To create virtual environment called `test-py3`, open the terminal (console, command prompt) and type one of the following
two commands:

    # creating virtual environment by using venv tool
    python3 -m venv test-py3
    # creating virtual environment by using virtualenv tool
    virtualenv test-py3

To activate the created virtual environment, type the following command:

    source test-py3/bin/activate

To deactivate the virtual environment, exit the terminal or type the command `deactivate`.

**NOTE:** There is no difference in using the python interpreter of virtual environment comparing to the using
system python interpreter.


### pip

The tool used for the installation of Python packages is [*pip*](https://pypi.org/project/pipa/).
It should come preinstalled with Python 3 interpreter. If not, consult [the official documentation
about the installation](https://pip.pypa.io/en/stable/installation/).

This sections assumes that you've recently created and activated `test-py3` virtual environment.
To see all packages installed, type the command:

    pip list
    # >>> The output should be liked this:
    # Package    Version
    # ---------- -------
    # pip        21.3
    # setuptools 58.2.0
    # wheel      0.37.0

To install new package (e.g. Django), type the following command:

    pip install Django

To uninstall the package (e.g. Django), type the following command:

    pip uninstall Django


### PyCharm IDE

The recommended IDE for Python development is [PyCharm](https://www.jetbrains.com/pycharm/download/#section=linux). Students that have e-mail addresses
with the *uns.ac.rs* domain are eligible to submit the request to receive free one-year license
for PyCharm Professional Edition.

