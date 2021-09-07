import tkinter as tk

from PIL import Image, ImageTk

import activateUsersFromCsvFile
import addGroup
import createUsersFromCsvFile
import deleteUsersFromCsvFile
import unlockAccounts

'''
This function display the frame of the main menu
'''


def display(connection):
    root = tk.Tk()
    root.title("Nicolas Alphonso : active directory automation script")

    canvas = tk.Canvas(root, width=1024, height=500)
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
    instructions.grid(column=0, row=1, columnspan=5)

    # add a group button
    add_group_text = tk.StringVar()

    add_group_button = tk.Button(root, textvariable=add_group_text, font="Raleway",
                                 command=lambda: addGroup.display(connection),
                                 bg="#20bebe", fg="white", height=2, width=10)
    add_group_text.set("Add a group")
    add_group_button.grid(column=0, row=2, columnspan=1)

    # Unlock accounts button
    unlock_accounts_text = tk.StringVar()
    unlock_accounts_button = tk.Button(root, textvariable=unlock_accounts_text, font="Raleway",
                                       command=lambda: unlockAccounts.unlock_accounts(connection),
                                       bg="#20bebe", fg="white", height=2, width=15)
    unlock_accounts_text.set("unlock accounts")
    unlock_accounts_button.grid(column=1, row=2, columnspan=1)

    # Create users from CSV button
    create_users_text = tk.StringVar()
    create_users_button = tk.Button(root, textvariable=create_users_text, font="Raleway",
                                    command=lambda: createUsersFromCsvFile.upload_action(connection),
                                    bg="#20bebe", fg="white", height=2, width=18)
    create_users_text.set("Add users from CSV")
    create_users_button.grid(column=2, row=2, columnspan=1)

    # Delete users from CSV button
    delete_users_text = tk.StringVar()
    delete_users_button = tk.Button(root, textvariable=delete_users_text, font="Raleway",
                                    command=lambda: deleteUsersFromCsvFile.upload_action(connection),
                                    bg="#20bebe", fg="white", height=2, width=18)
    delete_users_text.set("Delete users from CSV")
    delete_users_button.grid(column=3, row=2, columnspan=1)

    # Activate users from CSV button
    activate_users_text = tk.StringVar()
    activate_users_button = tk.Button(root, textvariable=activate_users_text, font="Raleway",
                                      command=lambda: activateUsersFromCsvFile.upload_action(connection),
                                      bg="#20bebe", fg="white", height=2, width=20)
    activate_users_text.set("Activate users from CSV")
    activate_users_button.grid(column=4, row=2, columnspan=1)

    root.mainloop()
