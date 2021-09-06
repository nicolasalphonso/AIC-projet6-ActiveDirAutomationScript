import tkinter as tk
from ldap3.core.exceptions import LDAPException
from dotenv import load_dotenv  # use of python-dotenv to hide credentials and use environment variables
load_dotenv()


def display(connection):
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Add a group")

    def add_user():
        # delete content of displayLabel
        result_display.config(text="")

        # retrieve data from form
        cn = input_cn.get()
        description = input_description.get()

        if (cn != "") and (description != ""):

            dl_shortname = cn
            dl_group_dn = 'CN=' + dl_shortname + ',DC=asertech,DC=fr'
            object_class = 'group'
            attr = {
                'cn': dl_shortname,
                'description': description,
                'groupType': '-2147483644',
                'sAMAccountName': dl_shortname
            }

            try:
                connection.add(dl_group_dn, object_class, attr)

            except LDAPException as e:
                connection.result['description'] = e

        else:
            connection.result['description'] = "All fields required"

        result_display.config(text=connection.result['description'])
        print(connection.result['description'])

    # main title
    title = tk.Label(root, text="Add a user", font=("Raleway", 30))
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
    add_group_button = tk.Button(root, text="Add user", font="Raleway",
                                 command=add_user(),
                                 bg="#20bebe", fg="white", height=2, width=10)

    add_group_button.pack()

    # result display
    result_display = tk.Label(root, text="", font=("Raleway", 22))
    result_display.pack()

    root.mainloop()