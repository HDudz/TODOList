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

        self.lists = load_todo_lists(self.file_path)

        self.name_var = ttk.StringVar()
        self.task_var = ttk.StringVar()
        self.tasks = []

        self.setup_AddFrame()

    def setup_AddFrame(self):
        """Sets up a list frame"""
        #Cleaning previous widgets
        self.addFrame.columnconfigure(0, weight=1)
        self.addFrame.columnconfigure((1, 2), weight=0)
        self.addFrame.rowconfigure(0, weight=0)



        for widget in self.addFrame.winfo_children():
            widget.destroy()

        addLabel = ttk.Label(self.addFrame, text="Adding new list", font=('roboto', 20), background=self.app.sec_color)
        nameLabel = ttk.Label(self.addFrame, text="List Name", font=('roboto', 15), background=self.app.sec_color)
        nameEntry = ttk.Entry(self.addFrame, textvariable=self.name_var, font=('roboto',15))
        taskLabel = ttk.Label(self.addFrame, text="Tasks", font=('roboto', 15), background=self.app.sec_color)


        addLabel.grid(column=0, row=0, columnspan=3, sticky='n', pady=(20, 10), padx=(20, 0))
        nameLabel.grid(column=0, row=1, columnspan=2, sticky="nw", pady=(10, 10), padx=(20, 0))
        nameEntry.grid(column=0, row=2, columnspan=2, sticky="nw", pady=(0, 10), padx=(20, 0))
        taskLabel.grid(column=0, row=3, columnspan=2, sticky="nw", pady=(10, 10), padx=(20, 0))

        for index, t in enumerate(self.tasks):
            tasksLabel = ttk.Label(self.addFrame, text="- "+t, font=('roboto', 12), background=self.app.sec_color)
            tasksLabel.grid(column=0, row=index+4, sticky='ew',  pady=(0, 10), padx=(20, 0))


        taskEntry = ttk.Entry(self.addFrame, textvariable=self.task_var, font=('roboto', 12))
        addButton = ttk.Button(self.addFrame, text="+", style="success", command=self.add_task)
        submitButton = ttk.Button(self.addFrame, text="Submit", style="success", width=10, command=self.submit)

        taskEntry.grid(column=0, row=len(self.tasks) + 4, columnspan=2, sticky="we", pady=(0, 10), padx=(20, 0))
        addButton.grid(column=2, row=len(self.tasks) + 4, sticky="we", pady=(0, 10), padx=(5, 20))
        submitButton.grid(column=0, row=len(self.tasks) + 6, pady=(5, 40),  sticky="s")



    def submit(self):
        self.lists.append({"title:", self.name_var}, {"todo", self.tasks})
        print(self.lists)

    def add_task(self):
        self.tasks.append(self.task_var.get())
        print(self.task_var.get())
        print(self.tasks)
        self.setup_AddFrame()
