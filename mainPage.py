import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from functions import load_todo_lists, delete_lists


class MainPage:
    def __init__(self, root):
        self.root = root
        self.file_path = 'lists.json'
        self.sec_color = "#444444"
        #Creating Frames
        self.mainPageFrame = ttk.Frame(root, style='secondary')
        self.listFrame = ttk.Frame(root, style='secondary')
        #GridingFrames
        self.mainPageFrame.grid(column=1, row=0, sticky="nwes")
        self.listFrame.grid(column=1, row=0, sticky="nwes")

        #Load lists from file
        self.lists = load_todo_lists(self.file_path)

        #Configure
        self.setup_mainPageFrame()
        self.switch_to_choice()



    def setup_mainPageFrame(self):
        """Configures main page frame"""
        self.mainPageFrame.columnconfigure(0, weight=1)
        self.mainPageFrame.columnconfigure((1,2), weight=0)
        self.mainPageFrame.rowconfigure(0, weight=0)

        for widget in self.mainPageFrame.winfo_children():
            widget.destroy()

        choiceLabel = ttk.Label(self.mainPageFrame, text="Choose your TODO List", font=('roboto', 20), background=self.sec_color)
        choiceLabel.grid(column=0, row=0, columnspan=3, sticky='n', pady=(20, 10), padx=(20, 0))

        for index, todo in enumerate(self.lists, start=1):
            title = todo['title']

            select_button = ttk.Button(self.mainPageFrame, text=title, width=20, style='light-outline' ,command=lambda t=title: self.switch_to_list(t))
            delete_button = ttk.Button(self.mainPageFrame, text="Delete", style="danger", width=9)
            delete_button.config(command=lambda t=title, i=index, selB=select_button, delB=delete_button: self.del_list(t, i, selB, delB))

            select_button.grid(column=0, row=index, sticky='ew', pady=(10, 0), padx=(20, 0))
            delete_button.grid(column=1, row=index, columnspan=2, sticky='ew', pady=(10, 0), padx=(0, 20))

        add_new_list_button = ttk.Button(self.mainPageFrame, text="Add new list", style="success")
        add_new_list_button.grid(column=0, row=len(self.lists) + 1, sticky='ew', pady=(10, 0), padx=(20, 0))


    def switch_to_choice(self):
        """Switches to choice page."""
        self.mainPageFrame.tkraise()

    def switch_to_list(self, title):
        """Switches to list page."""
        self.show_list_in_frame(title)
        self.listFrame.tkraise()

    def del_list(self, title, index, select_button, delete_button):
        def decide(decision):
            if decision:
                delete_lists(self.lists, title, self.file_path)
                self.lists = load_todo_lists(self.file_path)
                self.setup_mainPageFrame()
            else:
                confirmButton.destroy()
                delete_button.grid_configure(columnspan=2, column=1)
                select_button.configure(text=title)
                delete_button.configure(text="Delete", width=9, command=lambda t=title: self.del_list(t, index, select_button, delete_button))


        select_button.config(text="Are you sure you want to delete?")
        confirmButton = ttk.Button(self.mainPageFrame, text="Yes", style="success",width=3 , command=lambda: decide(True))
        confirmButton.grid(column=1, row=index, sticky='ew', pady=(10, 0))
        delete_button.config(text="No", width=3 ,command=lambda: decide(False))
        delete_button.grid_configure(column=2, columnspan=1)



    def show_list_in_frame(self, title):
        """Sets up a list frame"""
        #Cleaning previous widgets
        for widget in self.listFrame.winfo_children():
            widget.destroy()

        selected_list = next((todo for todo in self.lists if todo["title"] == title), None)

        if selected_list:
            titleLabel = ttk.Label(self.listFrame, text=selected_list["title"], font=('roboto', 20, 'bold'), background=self.sec_color)
            titleLabel.grid(column=0, row=0, pady=(20, 10), padx=(20, 0))

            for i, task in enumerate(selected_list["todo"], start=1):
                task_label = ttk.Label(self.listFrame, text=f"- {task}",
                                       font=('roboto', 14), background=self.sec_color)
                task_label.grid(column=0, row=i, sticky='w', padx=(20, 0))