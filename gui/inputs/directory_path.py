from tkinter import filedialog as fd
from tkinter.ttk import Label, Button

from gui.inputs.abstract.path import Path


class DirectoryPath(Path):
    """
      A class that renders the widgets that are related to accepting
      the path of the directory selected by the user.

      ...
      Methods
      -------
      render_widgets(r)
          Renders the widgets related to the input of the directory path.
      ask_for_path()
          Will open a filedialog for the user to select the desired
          directory in which the output of the program will be saved.
          The saved path will be of type string.

      ...
      Note; The setter for the video input file path of the bot
      is accessed through the parent_container.
      """

    def __init__(self, parent_container):
        """
        Parameter
        -------
        parent_container : Frame
            Where we will render our widgets into. Also, so we can access
            the bot property.
        """

        super().__init__(parent_container)

    def render_widgets(self, r):
        """
        Parameter
        -------
        r : int
            An integer to specify the row where we will render the widget.
        """

        Label(self.parent_container, text="Output directory: ") \
            .grid(sticky='w', row=r, column=1)

        self.entry.grid(sticky='w', ipadx=80, row=r, column=2, columnspan=3)

        Button(self.parent_container, text="Choose directory", command=lambda: self.ask_for_path()) \
            .grid(sticky='w', row=r, column=5)

    def ask_for_path(self):
        self.entry.delete(0, 'end')
        self.path = fd.askdirectory()
        self.entry.insert(0, self.path)

        self.parent_container.bot.set_output_dir(self.path)
