import ttkbootstrap as ttk
from functions import *


class ListPage:
    def __init__(self, app, title):
        self.app = app
        self.root = app.root
        self.title = title
        self.file_path = '../data/lists.json'
        self.frame = ttk.Frame(self.root, style='secondary')
        self.frame.grid(column=1, row=0, sticky="nwes")

        self.lists = load_todo_lists(self.file_path)

        self.setup()

    def setup(self):
        """Sets up a list frame"""
        #Cleaning previous widgets
        for widget in self.frame.winfo_children():
            widget.destroy()

        #Load lists from file
        self.lists = load_todo_lists(self.file_path)

        selected_list = next((todo for todo in self.lists if todo["title"] == self.title), None)

        if selected_list:
            titleLabel = ttk.Label(self.frame, text=selected_list["title"], font=('roboto', 20, 'bold'), background=self.app.sec_color)
            titleLabel.grid(column=0, row=0, pady=(20, 10), padx=(20, 0))

            for i, task in enumerate(selected_list["todo"], start=1):
                task_label = ttk.Label(self.frame, text=f"- {task}",
                                       font=('roboto', 14), background=self.app.sec_color)
                task_label.grid(column=0, row=i, sticky='w', padx=(20, 0))


    def show(self):
        self.setup()