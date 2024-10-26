import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from mainPage import MainPage
from menu import Menu

#Create and configure window and style
root = ttk.Window(themename="darkly")
root.geometry("800x600")
root.title("TODO List")
root.option_add("*font", "roboto")


root.columnconfigure(0, weight=0)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=1)


main_page = MainPage(root)
menu_page = Menu(root, main_page)


root.mainloop()
