import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mainPage
from mainPage import choicePage

#Create and configure window and style
root = ttk.Window(themename="todotheme")
root.geometry("800x600")
root.title("TODO List")
root.option_add("*font", "roboto")




root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)

menuFrame = ttk.Frame(root)
menuFrame.grid(column=0, row=0, sticky="nsew")

choicePage(root)

root.mainloop()
