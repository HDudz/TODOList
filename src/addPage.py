import ttkbootstrap as ttk
from functions import *


class AddPage:
    def __init__(self, app):
        self.app = app
        self.root = app.root

        self.file_path = '../data/lists.json'
        self.addFrame = ttk.Frame(self.root, style='secondary')
        self.addFrame.grid(column=1, row=0, sticky="nwes")
        self.addFrame.lower()

        self.setup_AddFrame()

    def setup_AddFrame(self):
        """Sets up a list frame"""
        #Cleaning previous widgets
        self.addFrame.columnconfigure(0, weight=1)
        self.addFrame.columnconfigure((1, 2), weight=0)
        self.addFrame.rowconfigure(0, weight=0)

        for widget in self.addFrame.winfo_children():
            widget.destroy()

        addLabel = ttk.Label(self.addFrame, text="Adding new frame", font=('roboto', 20),
                                background=self.app.sec_color)
        addLabel.grid(column=0, row=0, columnspan=3, sticky='n', pady=(20, 10), padx=(20, 0))
