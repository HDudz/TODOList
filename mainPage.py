import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json

file_path = 'lists.json'

def choicePage(root):
    def load_todo_lists(file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)

    def save_todo_lists(file_path, data):
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    lists = load_todo_lists(file_path)



    mainPageFrame = ttk.Frame(root, style='secondary')
    mainPageFrame.grid(column=1, row=0, sticky="nwes")


    #creating widgets
    choiceLabel = ttk.Label(mainPageFrame, text="Choose your TODO List", font=('roboto', 20), background="#3f4a56")

    #grid configure
    mainPageFrame.columnconfigure(0, weight=1)
    mainPageFrame.rowconfigure(0, weight=0)


    #packing widgets
    choiceLabel.grid(column=0, row=0, sticky='n', pady=(20, 20), padx=(20, 0))

    for index, todo in enumerate(lists, start=1):
        title = todo['title']
        select_button = ttk.Button(mainPageFrame, text=title, style='light-outline')
        delete_button = ttk.Button(mainPageFrame, text="Delete", bootstyle="danger")
        select_button.grid(column=0, row=index, sticky='ew', pady=(10, 0), padx=(10, 0))
        delete_button.grid(column=1, row=index, sticky='ew', pady=(10, 0), padx=(0, 10))


    add_new_list_button = ttk.Button(mainPageFrame, text="Add new list", bootstyle="success")
    add_new_list_button.grid(column=0, row=len(lists)+1, sticky='ew', pady=(10, 0), padx=(10, 0))