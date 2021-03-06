

# The Extensible Source Code Editor

The goal of this project is to develop an extensible source-code editor that is able to support syntax
highlighting. The highlighting depends on the programming language of source code program previewed to the user.


## Use Cases

When the application is started, the empty document (text area) is shown to the user.
The user can write some source code and save it to the location he/she chooses.
He/she is responsible to specify the extension that corresponds to the programming language of the source code program.
After the extension is specified, the code should be highlighted by the editor.

Beside creating a new source code file, the user can edit already persisted file on the disk.
When the file is loaded from the disk, the syntax highlighting should be done before the file content
is shown to the user.

Syntax highlighting should be done by the corresponding plugin. When the extension of the file
is recognized (no matter whether the file is saved after creating or loaded from the disk),
the corresponding plugin should be dynamically loaded to the application.
The plugin is responsible to apply syntax highlighting to the source code and show it to the user.
If the chosen file extension is not recognized by the editor, the appropriate
message box should be shown to the user and the code is previewed as a plain text.

At least three plugins for the following programming languages should be developed:

-   C
-   Python
-   Java


## Points Distribution

The project values 60 points in total:

-   (5 points) UML Class Diagram - the UML diagram of all classes in the application should be provided
-   (5 points) UML Component Diagram - the diagram of all components that exist in the application should be provided
-   (24 points) Plugins Implementation - Implementation of at least three plugins described above.
-   (14 points) Project Implementation - Implementation of the core editor component which is responsible to dynamically
    recognize and load the plugins. It is also responsible to load files from disk, save files to disk, etc.
-   (6 points) Git Tool Usage - The git tool is intended to be used by respecting the [GitFlow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow). More information can be found [here](https://github.com/vladaindjic/SCM-exchange-students#git).
-   (6 points) GitHub Platform Usage - To track down the project development, GitHub platform should be used. More information can be found [here](https://github.com/vladaindjic/SCM-exchange-students#github).


## Notes

The project is done individually. It should be hosted on the GitHub. The git version control
system should be used all the time.

The syntax highlighting should be done by using tags on text widget's text like [in this example](https://github.com/vladaindjic/SPC-exchange-students/blob/master/GUIAppExample/text_editor.py).

It is not allowed to use any kind of `highlight` functions implemented by someone else (e.g. [Pygments](https://pygments.org/)).

This is not the final version of the document and can be changed over time.

