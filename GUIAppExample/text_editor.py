from tkinter import Text, IntVar, Tk, INSERT, END

PATTERN_TO_MATCH = "text"
TAG_NAME = "red"


def process_key_press(e):
    # Some text has been typed to the SimpleTextEditor,
    # so rerun highlight_pattern method.
    e.widget.highlight_pattern(PATTERN_TO_MATCH, TAG_NAME)


class SimpleTextEditor(Text):
    """
    A text widget with a new method, highlight_pattern()

    example of using this class:
        # instantiate the class
        text = CustomText()
        # configuration of a tag that will be applied to the text
        text.tag_configure("red", foreground="#ff0000")
        # function that applies that to the text
        text.highlight_pattern("this should be red", "red")

    The highlight_pattern method is a simplified python
    version of the tcl code at http://wiki.tcl.tk/3246

    This class is taken from: https://stackoverflow.com/questions/3781670/how-to-highlight-text-in-a-tkinter-text-widget?fbclid=IwAR1YsDUOM4IoBaCVzMwbWGsVqX720gbviIaIB3z7PrgH8MUNOJatvIjyzVg
    """

    def __init__(self, *args, **kwargs):
        # https://stackoverflow.com/questions/18171328/how-to-use-super-when-subclassing-tkinter-widgets
        # See why super cannot be used
        Text.__init__(self, *args, **kwargs)
        # When key is pressed, the corresponding event is triggered and process by
        # the function
        self.bind('<KeyPress>', process_key_press)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        """
        Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        """

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = IntVar()
        while True:
            index = self.search(pattern, "matchEnd", "searchLimit",
                                count=count, regexp=regexp)
            if index == "":
                break
            if count.get() == 0:
                break  # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")


if __name__ == "__main__":
    # creating a root window
    root = Tk()
    root.title("Text Widget Example")
    # adding text field to root frame
    text = SimpleTextEditor(root, height=8)
    # fill the whole window
    text.pack()
    # insert some text programmatically
    text.insert(INSERT, "Some red text at the beginning.\n")
    text.insert(END, "More text at the end")
    # configure new tag that will be applied by highlight_pattern function
    text.tag_config("red", background="red", foreground="blue", font=("Georgia", "12", "bold"))
    # apply "red" tag to the text typed in text field
    text.highlight_pattern(PATTERN_TO_MATCH, TAG_NAME)
    # run the event loop which listens for the GUI events
    root.mainloop()
