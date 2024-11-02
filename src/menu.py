import ttkbootstrap as ttk
from functions import *


class Menu:
    def __init__(self, app, main_page):
        self.root = app.root
        self.main_page = main_page

        self.frame = ttk.Frame(self.root)
        self.frame.grid(column=0, row=0, sticky="nsew")

        self.buttonPadx = (5,5)

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure((0, 1, 2), weight=0)
        self.frame.rowconfigure(3, weight=1)

        self.titleLabel = ttk.Label(self.frame, text="  TODO\nManager", font=("roboto", 20, "bold", "italic"))
        self.choiceButton = ttk.Button(self.frame, text="Choose list", style="outline-light", command=lambda frame=self.main_page: switch_to(frame))
        self.settingsButton = ttk.Button(self.frame, text="Settings", style="outline-light")
        self.quitButton = ttk.Button(self.frame, text="Quit", style="outline-danger", command=self.root.destroy)

        self.titleLabel.grid(column=0, row=0, sticky="n", pady=(20, 10), padx=(35,35))
        self.choiceButton.grid(column=0, row=1, pady=(10, 5), padx=self.buttonPadx, sticky="ew")
        self.settingsButton.grid(column=0, row=2, pady=(5, 5), padx=self.buttonPadx, sticky="ew")
        self.quitButton.grid(column=0, row=3, pady=(5, 40), padx=self.buttonPadx, sticky="sew")



