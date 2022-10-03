from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

from .back import Converter


class ConverterFrontend(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.converter: Converter = Converter()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=2)

        self._create_widgets()

    def _create_widgets(self):
        self.raw_label: ttk.Label = ttk.Label(self, text="Raw Text")
        self.encoded_label: ttk.Label = ttk.Label(self, text="Base64")
        self.go_button: ttk.Button = ttk.Button(self, text="Go!")
        self.clear_button: ttk.Button = ttk.Button(self, text="Clear")
        self.raw_text: ScrolledText = ScrolledText(self)
        self.encoded_text: ScrolledText = ScrolledText(self)

        self.clear_button.bind("<Button-1>", self._clear_button)
        self.go_button.bind("<Button-1>", self._go_button)

        self.raw_label.grid(column=0, row=0)
        self.encoded_label.grid(column=1, row=0)
        self.raw_text.grid(column=0, row=1, sticky="NEWS")
        self.encoded_text.grid(column=1, row=1, sticky="NEWS")
        self.clear_button.grid(column=0, row=2, sticky="NEWS", padx=5, pady=5)
        self.go_button.grid(column=1, row=2, sticky="NEWS", padx=5, pady=5)

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
