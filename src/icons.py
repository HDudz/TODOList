from PIL import Image, ImageTk

class Icons:
    def load(self):
        self.whiteEdit = ImageTk.PhotoImage(Image.open('../data/whiteEdit.png').resize((20, 20)))
        self.blackEdit = ImageTk.PhotoImage(Image.open('../data/blackEdit.png').resize((20, 20)))
        self.whiteDel = ImageTk.PhotoImage(Image.open('../data/whiteDel.png').resize((20, 20)))
        self.blackDel = ImageTk.PhotoImage(Image.open('../data/blackDel.png').resize((20, 20)))
icons = Icons()