#importing all the necessary files, this list will get much bigger
import random
from textwrap import fill
import tkinter as tk
from tkinter import filedialog, Text
from tkinter import ttk
from turtle import fillcolor

#All the stuff you added is excellent Dante... all i did was add a tiny thing that says 'username'... all these functions I have in a string were just me playing around with tktinker haha... I'll delete them soon enough, but I was still having fun with them
""" 
def weird_checkerboard():
    for i in range(0, 800, 10):
        canvas.create_line(i, 0, i, 790, fill='blue', arrow='last')
    for i in range(0, 800, 10):
        canvas.create_line(0, i, 790, i, fill='red', arrow='last')
def curvy_shape_with_lines():
    for i in range(0, 800, 5):
        if i % 10 == 0:
            canvas.create_line(i, i, 0, 800 - i, fill='purple', arrow='both')
        else:
            canvas.create_line(800 - i, 0, i, i, fill='orange', arrow='both')
def sphere():
    for i in range(0, 200, 10):
        canvas.create_oval(200 + i, 200, 600 - i, 600, outline='purple')

def circles_fun():
    for i in range(0, 800, 5):
        canvas.create_oval(200, i, i, 800, outline='purple')
        canvas.create_oval(i, 200, 800, i, outline='orange')
        if i > 200 and i < 600:
            j = random.randrange(1, 3)
            canvas.create_oval(i - 200, i - (.7 * i), i + 200, 800, outline='green')
"""

#main tkinter file is stored in a variable called root_Quickeys
root_Quickeys = tk.Tk()
root_Quickeys.title=("Quickeys")
#this creates the canvas where we display "Quickeys" at the top of the screen. This is the tk.Canvas method
canvas = tk.Canvas(root_Quickeys, height=800, width=800, bg="#000000")
canvas.create_rectangle(0, 400, 800, 600, outline="green")
#this creates the green text: "Welcome To Quickeys" inside the canvas
canvas.create_text(400, 50, text="Welcome To Quickeys", fill="green", font="Helvetica 20 bold")
canvas.create_text(400, 500, text="Username?", fill="green", font="Helvetica 15 bold")


#this packs canvas with all the features(arguments we gave the tk.Canvas method)
canvas.pack()

#this command makes sure the program runs and also exits when we tell it to. (Captures Keystrokes I think)
root_Quickeys.mainloop()


