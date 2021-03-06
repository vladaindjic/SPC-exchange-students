

# GUI Desktop Application Devolopment in Python

To develop the GUI desktop application in Python, it is recommended
to use [`tkinter`](https://wiki.python.org/moin/TkInter). The installation instructions can be found [here](https://tkdocs.com/tutorial/install.html).
To test whether the installation is done properly, check
[*Verifying your Install* section](https://tkdocs.com/tutorial/install.html). Check *The Obligatory First Program*
section too.

A good starting point to learn some basics of tkinter library is to
consult the official [*TkDocs tutorial*](https://tkdocs.com/tutorial/).
The first example to examine can be found [here](https://tkdocs.com/tutorial/firstexample.html). 

**Note:** Don't spend to much time focusing on tkinter library concepts.
The goal of this course is not to learn tkinter, but to use
it as a context for developing the core of the extensible application
that actually do something useful.


# Text Editor in Tkinter

The [`text_editor.py`](https://github.com/vladaindjic/SPC-exchange-students/blob/master/GUIAppExample/text_editor.py) contains the implementation of a simple text editor
that is able to highlight some text that matches given pattern (word `text` in this case). 
Run the code and try to type some text. When the word `text` is typed,
it should be bolded, foreground should be set to blue, while the background is changed to red. 
The more information about the example can be found in the source code.

