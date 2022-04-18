from tkinter import Frame
from tkinter.ttk import Button

from gui.inputs.confidence import ConfidenceLevel
from gui.inputs.input_directory_path import InputDirectoryPath
from gui.inputs.input_file_path import InputFilePath
from gui.inputs.threshold import ThresholdLevel

"""
Here we will create our Menu page which is 
a child of Frame.

A Frame object needs a Tk object or another 
frame to render into (parent_container) here 
we will render into the container provided in app.
    
We will also accept app itself (controller) to 
access the show_frame method that will enable
us to switch pages.
"""


class Menu(Frame):
    def __init__(self, parent_container, controller, result, my_bot):
        super().__init__(parent_container)

        self.render_widgets(my_bot)

        Button(self, text="Start",
               command=lambda: controller.show_frame(result))\
            .grid(row=5, column=1, ipadx=15)

    def render_widgets(self, my_bot):
        InputFilePath(self, my_bot).render_input_file_widgets(1)
        InputDirectoryPath(self, my_bot).render_input_directory_widgets(2)
        ConfidenceLevel(self, my_bot).render_confidence_level_widgets(3)
        ThresholdLevel(self, my_bot).render_threshold_level_widgets(3)
