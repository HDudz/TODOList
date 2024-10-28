import ttkbootstrap as ttk
from functions import *


class Menu:
    def __init__(self, app, main_page):
        self.root = app.root
        self.main_page = main_page
        self.main_frame = self.main_page.mainPageFrame
        self.menuFrame = ttk.Frame(self.root)
        self.menuFrame.grid(column=0, row=0, sticky="nsew")

        self.buttonPadx = (5,5)

        self.menuFrame.columnconfigure(0, weight=1)
        self.menuFrame.rowconfigure((0, 1, 2), weight=0)
        self.menuFrame.rowconfigure(3, weight=1)

        self.titleLabel = ttk.Label(self.menuFrame, text="  TODO\nManager", font=("roboto", 20, "bold", "italic"))
        self.choiceButton = ttk.Button(self.menuFrame, text="Choose list", style="outline-light", command=lambda frame=self.main_frame: switch_to(frame))
        self.settingsButton = ttk.Button(self.menuFrame, text="Settings", style="outline-light")
        self.quitButton = ttk.Button(self.menuFrame, text="Quit", style="outline-danger", command=self.root.destroy)

        self.titleLabel.grid(column=0, row=0, sticky="n", pady=(20, 10), padx=(35,35))
        self.choiceButton.grid(column=0, row=1, pady=(10, 5), padx=self.buttonPadx, sticky="ew")
        self.settingsButton.grid(column=0, row=2, pady=(5, 5), padx=self.buttonPadx, sticky="ew")
        self.quitButton.grid(column=0, row=3, pady=(5, 40), padx=self.buttonPadx, sticky="sew")



