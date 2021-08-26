import tkinter as tk
from PIL import Image, ImageTk
import adduser


def buttontest():
    print("button works")

'''
This function display the frame of the main menu
'''

def display():

    root = tk.Tk()
    root.title("Nicolas Alphonso : active directory automation script")

    canvas = tk.Canvas(root, width=900, height=500)
    canvas.grid(columnspan=6, rowspan=5)

    # logo
    logo = Image.open('logo.png')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=0, row=0, columnspan=1)

    # main title
    title = tk.Label(root, text="Active Directory Automation Script", font=("Raleway", 30))
    title.grid(column=1, row=0, columnspan=5)

    # instructions
    instructions = tk.Label(root, text="Select a task below", font=("Raleway", 22))
    instructions.grid(column=1, row=1, columnspan=5)

    # add user button
    add_user_text = tk.StringVar()
    add_user_button = tk.Button(root, textvariable=add_user_text, font="Raleway", command=lambda: adduser.display(),
                                bg="#20bebe", fg="white", height=2, width=10)
    add_user_text.set("Add a user")
    add_user_button.grid(column=1, row=2, columnspan=1)

    # function2 button
    function2_text = tk.StringVar()
    function2_button = tk.Button(root, textvariable=function2_text, font="Raleway", command=lambda: buttontest(),
                                 bg="#20bebe", fg="white", height=2, width=10)
    function2_text.set("function 2")
    function2_button.grid(column=2, row=2, columnspan=1)

    # function3 button
    function3_text = tk.StringVar()
    function3_button = tk.Button(root, textvariable=function3_text, font="Raleway", command=lambda: buttontest(),
                                 bg="#20bebe", fg="white", height=2, width=10)
    function3_text.set("function 3")
    function3_button.grid(column=3, row=2, columnspan=1)

    # function4 button
    function4_text = tk.StringVar()
    function4_button = tk.Button(root, textvariable=function4_text, font="Raleway", command=lambda: buttontest(),
                                 bg="#20bebe", fg="white", height=2, width=10)
    function4_text.set("function 4")
    function4_button.grid(column=4, row=2, columnspan=1)

    # function5 button
    function5_text = tk.StringVar()
    function5_button = tk.Button(root, textvariable=function5_text, font="Raleway", command=lambda: buttontest(),
                                 bg="#20bebe", fg="white", height=2, width=10)
    function5_text.set("function 5")
    function5_button.grid(column=5, row=2, columnspan=1)

    root.mainloop()