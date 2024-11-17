from tkinter.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from functions import *
from icons import icons


class EditPage:
    def __init__(self, app, main_page, title):
        self.app = app
        self.root = app.root
        self.title = title
        self.main_page = main_page


        self.file_path = '../data/lists.json'
        self.frame = ttk.Frame(self.root, style='secondary')
        self.frame.grid(column=1, row=0, sticky="nwes")
        self.frame.lower()

        self.lists = load_todo_lists(self.file_path)

        self.selected_list = next((todo for todo in self.lists if todo["title"] == self.title), None)

        self.is_reset = True
        self.tasks = []


    def setup(self):
        """Sets up a list frame"""

        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=0)
        self.frame.rowconfigure(2, weight=1)

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.tasks = []

        editLabel = ttk.Label(self.frame, text="Editing list:", font=('roboto', 20, 'bold'), background=self.app.sec_color)
        self.nameEntry = ttk.Entry(self.frame, font=('roboto', 15))
        self.nameEntry.insert(0, self.title)

        editLabel.grid(column=0, row=0, sticky='n', pady=(20, 0), padx=(20, 0))
        self.nameEntry.grid(column=0, row=1, sticky='new', pady=(0, 30), padx=(100, 100))

        editFrame = ScrolledFrame(self.frame, style='secondary.TFrame', autohide=True)
        editFrame.grid(column=0, row=2, sticky="nwes")
        editFrame.container.configure(style="secondary.TFrame")
        editFrame.container.columnconfigure(0, weight=1)
        editFrame.container.columnconfigure(1, weight=0)




        for i, task in enumerate(self.selected_list["todo"], start=1):
            task_edit = ttk.Entry(editFrame.container, font=('roboto', 12))
            task_edit.insert(0, task)
            delete_button = ttk.Button(editFrame.container, style="danger", width=4, image=icons.whiteDel, compound=CENTER, command=lambda index=i - 1: self.delete_task(index) )


            task_edit.grid(column=0, row=i, sticky='ew', padx=(20, 0), pady=(10, 0))
            delete_button.grid(column=1, row=i, sticky='ew', padx=(0, 20), pady=(10, 0))

            self.tasks.append(task_edit)

        add_new_list_button = ttk.Button(editFrame.container, text="Add new task", style="success", command=self.add_new_task)
        add_new_list_button.grid(column=0, row=len(self.selected_list["todo"]) + 1, columnspan=1, sticky='ew', pady=(10, 0), padx=(20, 20))


        submitButton = ttk.Button(self.frame, text="Submit", style="success", width=10, command=self.submit)
        submitButton.grid(column=0, row=3, pady=(5, 40), sticky="s")

    def show(self):
        self.setup()
        self.frame.tkraise()

    def submit(self):
        self.selected_list["title"] = self.nameEntry.get()
        for i, task in enumerate(self.tasks, start=0):
            self.selected_list["todo"][i] = task.get()
        save_todo_lists(self.lists, self.file_path)
        self.main_page.show()

    def delete_task(self, index):
        del self.selected_list["todo"][index]
        self.setup()

    def add_new_task(self):
        self.selected_list["todo"].append("")
        self.setup()

