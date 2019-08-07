# Welcome to the Escape Room

This is a simple game with small scope created by Bob van den Berg for an Escape Room maker

## Installation

First download this zipfile and unzip it to a folder on your computer, for example:
C:\Users\EXAMPLEUSER\Downloads\EscapeRoomGarage

Install python 3.7.3 (tested) from
"https://www.python.org/downloads/"

(without quotation marks, also for the following commands)

Download the one relevant for your laptop. You can probably just click "Download Python 3.7.3" and it will download. For Windows laptops it will most probably be the 64 bit executable. During installation make sure that you've got the checkmark next to "add to PATH" checked.

Afterwards, on Windows, go to start and type "cmd" to open the command prompt.

Copy the path to the (EscapeRoomGarage) folder where the python files are and paste this like so in the command prompt:

```bash
cd C:/Users/EXAMPLEUSER/Downloads/EscapeRoomGarage
```

Replace EXAMPLEUSER with your username of your user folder.

When you have the workspace in your command prompt as your working directory, run this command:

```bash
py -m pip install playsound pygame pynput
```

to install the packages that are needed to run main.py, namely playsound, pygame and pynput.

## Usage

You're finished with installing all the required software. You can now run main.py by double-clicking it. You can also create a shortcut by right clicking main.py and copy to desktop.

## Secret codes / Solution

```python
SECRET_CODE = "5147"
HANDCUFF_CODE = "0807"
URL = 'https://www.locked-game.nl/test/form.html'
```

The secret codes for the game are hardcoded in main.py. If you want to edit them, open main.py with a text editor or IDE.

Have fun!

## Contributing

Pull requests are welcome.
