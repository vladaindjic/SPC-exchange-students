

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


## Notes

The project is done individually. It should be hosted on the GitHub. The git version control
system should be used all the time.
