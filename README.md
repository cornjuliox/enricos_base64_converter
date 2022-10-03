# About
This is a simple desktop app used to convert blocks of text to and from base64.

It's built on Python 3.10.4, GUI is built with Tkinter, and uses Python's built-in base64 module for its core functionality.

The Base64 output is url safe by default.


# How to Install
For now, this app is shipped as source. I assume you've got Python installed already and can do the following:

1. Clone the repository.
1. Create a venv (not required, but highly recommended) e.g `python -m venv .venv` and activate accordingly.
1. `pip install -r requirements.txt`
1. `python main.py` in the console/terminal to start the app. If all goes well you'll see the application window pop up

This app was tested on Windows 10, but should be cross-platform thanks to Python and Tkinter. If this isn't the case please let me know.


# How to Use
Usage is simple - if you want to convert plaintext to base64, paste the text into the text box on the left-hand side and hit the "Go" button.

If you want to convert base64 to plaintext, paste the base64 string ino the box on the right-hand side and hit the "Go" button.

For either option, the opposite text box has to be empty or you'll get an error. There's a "Clear" button in the lower left corner that will clear both text boxes.

