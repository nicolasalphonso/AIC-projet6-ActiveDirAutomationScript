import tkinter as tk
from PIL import Image, ImageTk


def display():
    root = tk.Tk()

    canvas = tk.Canvas(root, width=900, height=500)
    canvas.grid(columnspan=6, rowspan=5)

    # logo
    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0)

    root.mainloop()