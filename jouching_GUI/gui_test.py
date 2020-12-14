import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import io
import os

x = 100
y = 1000

root = tk.Tk()
root.title('fashion~')
root.geometry('+{}+{}'.format(x,y))
root.configure(background='beige')
root.resizable(width=True, height=True)

im1 = ImageTk.PhotoImage(Image.open('image1.jpg'))
im2 = ImageTk.PhotoImage(Image.open('image2.jpg'))
im3 = ImageTk.PhotoImage(Image.open('image3.jpg'))
list_im = [im1, im2, im3]

label = Label(image=im1)
label.grid(row=1, column=0, columnspan=3)
button_back = tk.Button(root, text="Back")
button_exit = Button(root, text="Exit")
button_forward = tk.Button(root, text="Forward")
# button_forward.pack()

root.mainloop()
