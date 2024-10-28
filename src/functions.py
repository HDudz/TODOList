import json


def load_todo_lists(file_path):
    """Loads lists from JSON."""
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

def save_todo_lists(lists, file_path):
    """Saves lists to JSON."""
    json_object = json.dumps(lists, indent=4)
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_object)

def delete_lists(lists, title, file_path):
    selected_list = next((todo for todo in lists if todo["title"] == title), None)
    if selected_list:
        lists.remove(selected_list)
        save_todo_lists(lists, file_path)

def switch_to(frame):
    frame.tkraise()