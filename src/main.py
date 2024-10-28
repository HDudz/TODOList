import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from mainPage import MainPage
from menu import Menu

class App:
    sec_color = "#444444"
    font = ("*font", "roboto")

    def __init__(self):
        # Create and configure window and style
        self.root = ttk.Window(themename="darkly")
        self.root.geometry("800x600")
        self.root.title("TODO List")
        self.root.option_add("*font", "roboto")

        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=2)
        self.root.rowconfigure(0, weight=1)


        self.main_page = MainPage(self)
        self.menu_page = Menu(self, self.main_page)

        self.root.mainloop()

app = App()
