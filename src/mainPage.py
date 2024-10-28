import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from functions import *
from PIL import Image, ImageTk
from listPage import ListPage
from addPage import AddPage


class MainPage:
    def __init__(self, app):
        self.app = app
        self.root = app.root
        self.file_path = '../data/lists.json'
        whiteEdit_path = '../data/whiteEdit.png'
        blackEdit_path = '../data/blackEdit.png'
        whiteDel_path = '../data/whiteDel.png'
        blackDel_path = '../data/blackDel.png'


        # Rescaling
        white_edit_img = Image.open(whiteEdit_path).resize((20, 20))
        black_edit_img = Image.open(blackEdit_path).resize((20, 20))
        white_del_img = Image.open(whiteDel_path).resize((20, 20))
        black_del_img = Image.open(blackDel_path).resize((20, 20))

        self.whiteDelImg = ImageTk.PhotoImage(white_del_img)
        self.blackDelImg = ImageTk.PhotoImage(black_del_img)
        self.whiteEditImg = ImageTk.PhotoImage(white_edit_img)
        self.blackEditImg = ImageTk.PhotoImage(black_edit_img)

        #Creating Frames
        self.mainPageFrame = ttk.Frame(self.root, style='secondary')

        #GridingFrames
        self.mainPageFrame.grid(column=1, row=0, sticky="nwes")

        #Load lists from file
        self.lists = load_todo_lists(self.file_path)

        #Configure
        self.setup_mainPageFrame()



    def setup_mainPageFrame(self):
        """Configures main page frame"""
        self.mainPageFrame.columnconfigure(0, weight=1)
        self.mainPageFrame.columnconfigure((1,2), weight=0)
        self.mainPageFrame.rowconfigure(0, weight=0)

        self.add_page = AddPage(self.app)

        for widget in self.mainPageFrame.winfo_children():
            widget.destroy()

        choiceLabel = ttk.Label(self.mainPageFrame, text="Choose your TODO List", font=('roboto', 20), background=self.app.sec_color)
        choiceLabel.grid(column=0, row=0, columnspan=3, sticky='n', pady=(20, 10), padx=(20, 0))

        for index, todo in enumerate(self.lists, start=1):
            title = todo['title']
            select_button = ttk.Button(self.mainPageFrame, text=title, width=20, style='light-outline' ,command=lambda t=title: self.switch_to_list(t))
            edit_button = ttk.Button(self.mainPageFrame, style="primary", width=4, image=self.whiteEditImg, compound=CENTER)
            delete_button = ttk.Button(self.mainPageFrame, style="danger", width=4, image=self.whiteDelImg, compound=CENTER)
            delete_button.config(command=lambda t=title, i=index, selB=select_button: self.del_list(t, i, selB))

            select_button.grid(column=0, row=index, sticky='ew', pady=(10, 0), padx=(20, 0))
            edit_button.grid(column=1, row=index, sticky='ew',  pady=(10, 0))
            delete_button.grid(column=2, row=index, sticky='ew', pady=(10, 0), padx=(0, 20))

        add_new_list_button = ttk.Button(self.mainPageFrame, text="Add new list", style="success", command=self.switch_to_adding)
        add_new_list_button.grid(column=0, row=len(self.lists) + 1, columnspan = 1, sticky='ew', pady=(10, 0), padx=(20, 0))




    def del_list(self, title, index, select_button):
        def decide(decision):
            if decision:
                delete_lists(self.lists, title, self.file_path)
                self.lists = load_todo_lists(self.file_path)
                self.setup_mainPageFrame()
            else:
                confirmButton.destroy()
                declineButton.destroy()
                select_button.configure(text=title)


        select_button.config(text="Are you sure you want to delete?")
        confirmButton = ttk.Button(self.mainPageFrame, text="Yes", style="success", width=4, command=lambda: decide(True))
        confirmButton.grid(column=1, row=index, sticky='ew', pady=(10, 0))
        declineButton = ttk.Button(self.mainPageFrame, text="No", style="danger", width=4, command=lambda: decide(False))
        declineButton.grid(column=2, row=index, sticky='ew', pady=(10, 0), padx=(0, 20))

    def switch_to_list(self, title):
        list_page = ListPage(self.app, title)
        switch_to(list_page.listFrame)
    def switch_to_adding(self):
         switch_to(self.add_page.addFrame)


