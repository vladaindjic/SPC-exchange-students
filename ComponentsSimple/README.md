

# Simple Extensible Application

This Python project represents an example of using setuptools for developing simple extensible/pluggable application
in Python programming language.

The application consists of three components:

-   `Core`
-   `AddOperator`
-   `SubstractOperator`


## `Core`

[`Core` component](https://github.com/vladaindjic/SPC-exchange-students/tree/master/ComponentsSimple/Core) specifies an [abstract implementation of a mathematical operator](https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/Core/plugin/operator/core/services/operator.py).
It also specifies [the script](https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/Core/plugin/operator/core/console_main.py) that can be run from the terminal/console upon installation.

To install this component, `cd Core` and run `python setup.py install`. After this
the script can be run with `operator_main`. As you may notice, the script
prints the message *No available plugins*, because none of the plugins have been installed. 


## `AddOperator`


## `SubtractOperator`


## Note

The more explanation about the components can be found in the source code.

