import ttkbootstrap as ttk
from scipy.constants import value

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

        style = ttk.Style()
        style.configure(
            'MyCheckbutton.success.TCheckbutton',
            font=('roboto', 14),
            background=self.app.sec_color,
            foreground='white'
        )

        style.map('TCheckbutton', foreground=[
            ('disabled', 'white'),
            ('selected', 'yellow'),
            ('!selected', 'gray')])

        selected_list = next((todo for todo in self.lists if todo["title"] == self.title), None)

        if selected_list:
            titleLabel = ttk.Label(self.frame, text=selected_list["title"], font=('roboto', 20, 'bold'), background=self.app.sec_color)
            titleLabel.grid(column=0, row=0, columnspan=2, pady=(20, 10), padx=(20, 0))

            for i, task in enumerate(selected_list["todo"], start=1):
                task_var = ttk.BooleanVar(value=task["done"])
                def toggle_done(task=task, var=task_var):
                    task["done"] = var.get()
                    save_todo_lists(self.lists, self.file_path)

                task_check = ttk.Checkbutton(
                    self.frame,
                    variable=task_var,
                    onvalue=True,
                    offvalue=False,
                    style='MyCheckbutton.success.TCheckbutton',
                    command = toggle_done,
                )
                task_label = ttk.Label(self.frame, text=task['task'],
                                       font=('roboto', 14), background=self.app.sec_color)
                task_check.grid(column=0, row=i, sticky='w', padx=(20, 0))
                task_label.grid(column=1, row=i, sticky='w', padx=(0, 0))


    def show(self):
        self.setup()
        self.frame.tkraise()
