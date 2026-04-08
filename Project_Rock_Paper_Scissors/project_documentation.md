# Rock, Paper, Scissors + Kirby Victory (Project)

Welcome to my version of Rock, Paper, Scissors! This is an interactive project developed in **Python** that combines classic programming logic with fun, ASCII-style icons. This program or game includes a surprise graphical interface upon winning, making victory more satisfying, or rather, more fun, I would say.

## Features
- **Game Logic:** Basic system: User versus computer using `random`, allowing you to choose rock, paper, or scissors at random.

- **Graphical Interface (GUI):** A special, creative window as a reward for winning the game. The library used was `tkinter`.

- **ASCII Art:** Visual representation of the game tools in the terminal.

- **Modularization:** Separation of the game logic and the interface into different files for cleaner code.

## Technologies Used
- **Python 3.x**
- **Tkinter** (For the interface, which is the victory window).

- **OS & Random** (Native Python libraries).

## Project Structure
- `main.py`: This is the heart of the game, running in the terminal, where the Rock, Paper, Scissors logic takes place.

- `Kirby_Victory.py`: Module that manages the pink congratulations window with Kirby's image.

- `HappyKirby.png`: Visual resource for the victory screen.

## How to Play
1. Clone this repository or download the files.

2. Make sure you have the `HappyKirby.png` image in the same folder as the scripts so that the scripts that generate the interface work.

3. Run the main file:
```Tap
python main.py <- This script is the main program that runs the entire game.

## Commands Used in the Project (Important to Remember)

- import random: Imports the library for generating random numbers. We use it so the computer chooses between Rock, Paper, Scissors.

- .capitalize(): This is a text method. It transforms what the user types (e.g., "rock") into title format ("Rock"), so it always matches your list.

- random.choice(option): Takes the list of options within the program and chooses a random element. In this case, it would be the CPU, which would be our opponent.

- if / elif / else: These are conditional statements. They control the flow of the game: whether the user wins, ties, or types something that doesn't exist.

## Interface Commands

NOTE: These commands are new to me, so I've included their literal Python function for some of them.

- import tkinter as tk: Loads the library for creating windows. I use `as tk` to avoid having to type `tkinter` all the time, which I found a bit more practical.

- `win = tk.Tk()`: Creates the main window (the interface).

- `win.geometry("500x500")`: Defines the window size in pixels (Width x Height).

- `win.configure(bg="#FFB7C5")`: Changes the background color. `bg` stands for Background.

- `tk.Label(...)`: Creates a label. This can be used for both text and images.

- `tk.Button(...)`: Creates the interactive button. The parameter `command=win.destroy` is what makes the window close when clicked.

## File and Path Commands

- `import os`: Library for interacting with the operating system (folders and files). - os.path.dirname(__file__): Automatically detects the folder where the currently running .py file is located.

- os.path.join(path, name): Securely joins the folder name with the image name.

- tk.PhotoImage(file=...): This command loads the image from the hard drive into Python's memory so it can be displayed.

## Control Commands

- .pack(): The "packer". Without it, the object exists but isn't drawn in the window, which is what's needed for a creative look, in my opinion. It arranges the elements one below the other.

- pady=20: Adds a vertical margin (space above and below) so the elements aren't crowded.

- win.mainloop(): This is the window engine. It keeps the program running and listening for clicks. Without it, the window would open and close in a millisecond.

- if __name__ == "__main__":: In this case, this was the most important command to use. It prevents the Kirby_Victory.py window from opening automatically when the main program imports it upon execution. It only allows it to open if you run the main program and call Kirby_Victory() correctly.