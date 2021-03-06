

# Simple Extensible Application

This Python project represents an example of using setuptools for developing simple extensible/pluggable application
in Python programming language.

The application consists of three components:

-   `Core`
-   `AddOperator`
-   `SubstractOperator`

The component diagram of this extensible application can be found [here](https://github.com/vladaindjic/SPC-exchange-students/tree/master/ComponentsSimple/diagrams).


## `Core`

[`Core` component](https://github.com/vladaindjic/SPC-exchange-students/tree/master/ComponentsSimple/Core) specifies [an abstract implementation of a mathematical operator](https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/Core/plugin/operator/core/services/operator.py).
It also specifies [the script](https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/Core/plugin/operator/core/console_main.py) that can be run from the terminal/console upon installation.

To install this component, `cd Core` and run `python setup.py install`. After this
the script can be run with `operator_main`. As you may notice, the script
prints the message *No available plugins*, because none of the plugins have been installed. 


## `AddOperator`

[`AddOperator` component](https://github.com/vladaindjic/SPC-exchange-students/tree/master/ComponentsSimple/AddOperator) specifies [a concrete implementation of a mathematical addition operator](https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/AddOperator/plugin/operator/addition/add_operator.py).

To install this component, `cd AddOperator` and run `python setup.py install`. After this
run the `operator_main` command in the terminal. As you may notice, the `AddOperator`
is recognized as plugin and loaded in Core component, so you may add two integers. 


## `SubtractOperator`

[`SubtractOperator` component](https://github.com/vladaindjic/SPC-exchange-students/tree/master/ComponentsSimple/SubtractOperator) specifies [a concrete implementation of a mathematical subtraction operator](https://github.com/vladaindjic/SPC-exchange-students/blob/master/ComponentsSimple/SubtractOperator/plugin/operator/subtraction/subtract_operator.py).

To install this component, `cd SubtractOperator` and run `python setup.py install`. After this
run the `operator_main` command in the terminal. As you may notice, the `SubtractOperator`
is recognized as plugin and loaded in Core component, so you may apply subtraction on two integers. 


## Note

The more explanation about the components can be found in the source code.


## Task for Students

Try to extend the given example with the plugins that implement multiplication and division operators.

