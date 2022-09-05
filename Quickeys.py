#importing all the necessary files, this list will get much bigger
import tkinter as tk
from tkinter import filedialog, Text

#main tkinter file is stored in a variable called root_Quickeys
root_Quickeys = tk.Tk()

#this creates the canvas where we display "Quickeys" at the top of the screen. This is the tk.Canvas method
canvas = tk.Canvas(root_Quickeys, height=800, width=800, bg="#000000")

#this creates the green text: "Welcome To Quickeys" inside the canvas
canvas.create_text(300, 50, text="Welcome To Quickeys", fill="green", font="Helvetica 20 bold")

#this packs canvas with all the features(arguments we gave the tk.Canvas method)
canvas.pack()

#this command makes sure the program runs and also exits when we tell it to. (Captures Keystrokes I think)
root_Quickeys.mainloop()