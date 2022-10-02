from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # NOTE: this has to be explicitly imported and won't be brought in with the star import.
from tkinter.scrolledtext import ScrolledText

from base64converter.back import Converter


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

class ConverterFrontend(ttk.Frame):
    # TODO: Move this class into the 'front' module
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.converter = Converter()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=2)

        self._create_widgets()

    def _create_widgets(self):
        self.raw_label = ttk.Label(self, text="Raw Text")
        self.encoded_label = ttk.Label(self, text="Base64")
        self.go_button = ttk.Button(self, text="Go!")
        self.clear_button = ttk.Button(self, text="Clear")
        self.raw_text = ScrolledText(self)
        self.encoded_text = ScrolledText(self)

        self.clear_button.bind("<Button-1>", self._clear_button)
        self.go_button.bind("<Button-1>", self._go_button)

        self.raw_label.grid(column=0, row=0)
        self.encoded_label.grid(column=1, row=0)
        self.raw_text.grid(column=0, row=1, sticky=(N, E, W, S))
        self.encoded_text.grid(column=1, row=1, sticky=(N, E, W, S))
        self.clear_button.grid(column=0, row=2, sticky=(N, E, W, S))
        self.go_button.grid(column=1, row=2, sticky=(N, E, W, S))

    def _clear_button(self, event):
        self.raw_text.delete(1.0, END)
        self.encoded_text.delete(1.0, END)
        return

    def _go_button(self, event):
        # first determine which operation to perform
        # if both boxes have text, we cannot proceed and must display
        # an error message
        check_1: bool = self._is_raw_text_empty()
        check_2: bool = self._is_encoded_text_empty()
        # TODO: Change this to a proper logger
        print(check_1)
        print(check_2)
        print()

        if check_1 and check_2:
            messagebox.showinfo("Error!", "Write/paste text into either box before hitting 'Go!'.")
            return

        if check_1 is False and check_2 is False:
            messagebox.showinfo("Error!", "Only one box should have text! Clear one and try again.")
            return
        
        if check_1 is False:
            raw_input: str = self.raw_text.get("1.0", END)
            encoded: str = self.converter.encode(raw_input)
            self.encoded_text.insert(END, encoded)
            return
        
        if check_2 is False:
            raw_input: str = self.encoded_text.get("1.0", END)
            encoded: str = self.converter.decode(raw_input)
            self.raw_text.insert(END, encoded)
            return

    # NOTE: There might be a better way to organize this
    def _is_raw_text_empty(self) -> bool:
        return self.raw_text.compare("end-1c", "==", "1.0")

    def _is_encoded_text_empty(self) -> bool:
        return self.encoded_text.compare("end-1c", "==", "1.0")


if __name__ == "__main__":
    # root setup
    root = MainApp()

    # content
    content = ConverterFrontend(root)
    content.grid(column=0, row=0, sticky=(N, E, W, S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    root.mainloop()
