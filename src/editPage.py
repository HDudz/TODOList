import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from functions import *


class EditPage:
    def __init__(self, app, title):
        self.app = app
        self.root = app.root
        self.title = title

        self.file_path = '../data/lists.json'
        self.frame = ttk.Frame(self.root, style='secondary')
        self.frame.grid(column=1, row=0, sticky="nwes")
        self.frame.lower()

        self.lists = load_todo_lists(self.file_path)

        self.is_reset = True
        self.tasks = []


    def setup(self):
        """Sets up a list frame"""

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(2, weight=1)

        for widget in self.frame.winfo_children():
            widget.destroy()



        editLabel = ttk.Label(self.frame, text="Editing list:", font=('roboto', 20, 'bold'), background=self.app.sec_color)
        nameEntry = ttk.Entry(self.frame, font=('roboto', 15))
        nameEntry.insert(0, self.title)

        editLabel.grid(column=0, row=0, sticky='n', pady=(20, 0), padx=(20, 0))
        nameEntry.grid(column=0, row=1, sticky='new', pady=(0, 30), padx=(100, 100))

        editFrame = ScrolledFrame(self.frame, style='secondary.TFrame', autohide=True)
        editFrame.grid(column=0, row=2, sticky="nwes")
        editFrame.container.configure(style="secondary.TFrame")
        editFrame.container.columnconfigure(0, weight=1)


        selected_list = next((todo for todo in self.lists if todo["title"] == self.title), None)

        for i, task in enumerate(selected_list["todo"], start=1):
            task_edit = ttk.Entry(editFrame.container, font=('roboto', 12))
            task_edit.insert(0, task)
            task_edit.grid(column=0, row=i, sticky='ew', padx=(20, 20), pady=(0, 10))
            self.tasks.append(task_edit)

        submitButton = ttk.Button(self.frame, text="Submit", style="success", width=10)
        submitButton.grid(column=0, row=3, pady=(5, 40), sticky="s")

    def show(self):
        self.setup()
        self.frame.tkraise()