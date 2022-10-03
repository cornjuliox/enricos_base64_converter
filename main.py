from tkinter import *
from tkinter import messagebox  # NOTE: this has to be explicitly imported and won't be brought in with the star import.

from base64converter.front import ConverterFrontend


class MainApp(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Enrico's Base64 Converter")
        self.option_add("*tearOff", FALSE)
        self._create_menu()

    def _create_menu(self):
        menubar = Menu(self)
        sysmenu = Menu(menubar, name="system")
        menu_about = Menu(menubar)
        menu_about.add_command(label="About", command=self._about)
        menubar.add_cascade(menu=menu_about, label="Help")
        menubar.add_cascade(menu=sysmenu)

        self["menu"] = menubar

    def _about(self):
        messagebox.showinfo("About this program", "Created by Enrico Tuvera Jr on October 3, 2022")

if __name__ == "__main__":
    # root setup
    root: MainApp = MainApp()

    # content
    content: ConverterFrontend = ConverterFrontend(root)
    content.grid(column=0, row=0, sticky="NEWS")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()
