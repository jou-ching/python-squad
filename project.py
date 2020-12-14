import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

app = tk.Tk()
medium_font = tkFont.Font(family="Courier", size=16)
app.option_add("*TCombobox*Listbox*Font", medium_font)

app.geometry("720x360")
app.title("Your Stylist")
label = tk.Label(app, text = "Choose what you like!!")
label.pack()
label.config(font = ("AR CENA",32))
choose = ttk.Combobox(app, values = ["野餐","韓系","日系"], width = 40)
choose.pack(pady = 20)
next_button = tk.Button(app, text = "next step")
next_button.pack(pady = 20)
app.mainloop()