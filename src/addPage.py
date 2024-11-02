import ttkbootstrap as ttk
from functions import *


class AddPage:
    def __init__(self, app, main_page):
        self.app = app
        self.root = app.root
        self.main_page = main_page

        self.file_path = '../data/lists.json'
        self.frame = ttk.Frame(self.root, style='secondary')
        self.frame.grid(column=1, row=0, sticky="nwes")
        self.frame.lower()

        self.lists = load_todo_lists(self.file_path)

        self.is_reset = True

        self.name_var = ttk.StringVar()
        self.task_var = ttk.StringVar()
        self.tasks = []

        self.setup()

    def setup(self):
        """Sets up a list frame"""
        #Cleaning previous widgets

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure((1, 2), weight=0)
        self.frame.rowconfigure(0, weight=0)


        self.lists = load_todo_lists(self.file_path)

        if self.is_reset:
            self.name_var.set("")
            self.task_var.set("")
            self.tasks.clear()
            self.is_reset = False


        for widget in self.frame.winfo_children():
            widget.destroy()


        addLabel = ttk.Label(self.frame, text="Adding new list", font=('roboto', 20), background=self.app.sec_color)
        nameLabel = ttk.Label(self.frame, text="List Name", font=('roboto', 15), background=self.app.sec_color)
        nameEntry = ttk.Entry(self.frame, textvariable=self.name_var, font=('roboto', 15))
        taskLabel = ttk.Label(self.frame, text="Tasks", font=('roboto', 15), background=self.app.sec_color)


        addLabel.grid(column=0, row=0, columnspan=3, sticky='n', pady=(20, 10), padx=(20, 0))
        nameLabel.grid(column=0, row=1, columnspan=2, sticky="nw", pady=(10, 10), padx=(20, 0))
        nameEntry.grid(column=0, row=2, columnspan=2, sticky="nw", pady=(0, 10), padx=(20, 0))
        taskLabel.grid(column=0, row=3, columnspan=2, sticky="nw", pady=(10, 10), padx=(20, 0))

        for index, t in enumerate(self.tasks):
            tasksLabel = ttk.Label(self.frame, text="- " + t, font=('roboto', 12), background=self.app.sec_color)
            tasksLabel.grid(column=0, row=index+4, sticky='ew',  pady=(0, 10), padx=(20, 0))


        taskEntry = ttk.Entry(self.frame, textvariable=self.task_var, font=('roboto', 12))
        addButton = ttk.Button(self.frame, text="+", style="success", command=self.add_task)
        submitButton = ttk.Button(self.frame, text="Submit", style="success", width=10, command=self.submit)

        taskEntry.grid(column=0, row=len(self.tasks) + 4, columnspan=2, sticky="we", pady=(0, 10), padx=(20, 0))
        addButton.grid(column=2, row=len(self.tasks) + 4, sticky="we", pady=(0, 10), padx=(5, 20))
        submitButton.grid(column=0, row=len(self.tasks) + 6, pady=(5, 40),  sticky="s")

    def show(self):
        self.is_reset = True
        self.setup()

    def submit(self):
        add_lists(self.name_var.get(), self.tasks, self.file_path)
        self.main_page.show()

    def add_task(self):
        self.tasks.append(self.task_var.get())
        print(self.task_var.get())
        print(self.tasks)
        self.setup()
