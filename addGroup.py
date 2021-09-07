import os
import time
import tkinter as tk

# use of python-dotenv to hide credentials and use environment variables
from dotenv import load_dotenv
from ldap3.core.exceptions import LDAPException

import logsManagement

load_dotenv()

'''
This function displays the form and calls the function to create a group
'''


def display(connection):
    # generate the window
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Add a group")

    '''
    This function handles the creation of a group
    '''

    def add_a_group():
        # determine a good time based complement for the log filename
        initial_time = time.strftime("%Y%m%d-%H%M%S")

        # define the first line of the log file
        initial_log = "Logs: Add a group " + initial_time
        logs = initial_log

        # delete content of displayLabel
        result_display.config(text="")

        # retrieve data from form
        cn = input_cn.get()
        description = input_description.get()

        # if fields are not empty
        if (cn != "") and (description != ""):

            # generate the dn and the attribute of the new group
            dl_group_dn = 'CN=' + cn + os.environ.get("SEARCHDC")
            object_class = 'group'
            attr = {
                'cn': cn,
                'description': description,
                'groupType': '-2147483644',
                'sAMAccountName': cn
            }

            # add the group
            try:
                connection.add(dl_group_dn, object_class, attr)

            except LDAPException as e:
                connection.result['description'] = e

        # else display that all fields are required
        else:
            connection.result['description'] = "All fields required"

        # display the description of the result of the operation
        info_to_display = "\nGroup \"" + cn + "\" creation : " + connection.result['description']
        result_display.config(text=info_to_display)
        logs += info_to_display

        # print and write logs
        logsManagement.write_logs(logs, initial_log, initial_time, "create_group")

        # empty form
        input_cn.delete(0, 'end')
        input_description.delete(0, 'end')

    # main title
    title = tk.Label(root, text="Add a group", font=("Raleway", 30))
    title.pack()

    # instructions
    instructions = tk.Label(root, text="Fill the form then press the button", font=("Raleway", 22))
    instructions.pack()

    # form
    # form cn part
    cn_label = tk.Label(root, text="cn :")
    cn_label.pack()
    input_cn = tk.Entry(root, width=40)
    input_cn.pack(pady=20)

    # form description part
    input_description_label = tk.Label(root, text="description :")
    input_description_label.pack()
    input_description = tk.Entry(root, width=40)
    input_description.pack(pady=20)

    # "add a group" button
    add_group_button = tk.Button(root, text="Add group", font="Raleway",
                                 command=add_a_group,
                                 bg="#20bebe", fg="white", height=2, width=10)

    add_group_button.pack()

    # result display
    result_display = tk.Label(root, text="", font=("Raleway", 22))
    result_display.pack()

    # tkinter main loop
    root.mainloop()
