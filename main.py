from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # NOTE: this has to be explicitly imported and won't be brought in with the star import.

from base64converter.back import Converter


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Enrico's Base64 Converter")
        self.option_add("*tearOff", FALSE)
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self)
        sysmenu = Menu(menubar, name="system")
        menu_about = Menu(menubar)
        menu_about.add_command(label="About", command=self.about)
        menubar.add_cascade(menu=menu_about, label="Help")
        menubar.add_cascade(menu=sysmenu)

        self["menu"] = menubar

    def about(self):
        messagebox.showinfo("About this program", "Created by Enrico Tuvera Jr on October 3, 2022")

class ConverterFrontend(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.converter = Converter()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=2)
        
        self.create_widgets()

    def create_widgets(self):
        self.raw_label = ttk.Label(self, text="Raw Text")
        self.encoded_label = ttk.Label(self, text="Base64")
        self.go_button = ttk.Button(self, text="Go!")
        self.raw_text = Text(self)
        self.encoded_text = Text(self)

        self.raw_label.grid(column=0, row=0)
        self.encoded_label.grid(column=1, row=0)
        self.raw_text.grid(column=0, row=1, sticky=(N, E, W, S))
        self.encoded_text.grid(column=1, row=1, sticky=(N, E, W, S))
        self.go_button.grid(column=1, row=2, sticky=(N, E, W, S))

if __name__ == "__main__":
    # root setup
    root = MainApp()

    # content
    content = ConverterFrontend(root)
    content.grid(column=0, row=0, sticky=(N, E, W, S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()
