import ttkbootstrap as ttk


class Menu:
    def __init__(self, root, main_page):
        menuFrame = ttk.Frame(root)
        menuFrame.grid(column=0, row=0, sticky="nsew")

        menuFrame.columnconfigure(0, weight=1)
        menuFrame.rowconfigure((0, 1), weight=0)

        titleLabel = ttk.Label(menuFrame, text="  TODO\nManager", font=("roboto", 20, "bold", "italic"))
        choiceButton = ttk.Button(menuFrame, text="Choose list", style="outline-light", command=main_page.switch_to_choice)
        settingsButton = ttk.Button(menuFrame, text="Settings", style="outline-light")

        titleLabel.grid(column=0, row=0, sticky="n", pady=(20, 10), padx=(35,35))
        choiceButton.grid(column=0, row=1, pady=(10, 5), sticky="ew")
        settingsButton.grid(column=0, row=2, pady=(5, 10), sticky="ew")
