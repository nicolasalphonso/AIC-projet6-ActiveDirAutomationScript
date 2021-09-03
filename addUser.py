import tkinter as tk
from dotenv import load_dotenv  # use of python-dotenv to hide credentials and use environment variables
load_dotenv()
from ldap3.core.exceptions import LDAPException, LDAPBindError

def display(connection):
    root = tk.Tk()
    root.geometry("900x500")
    root.title("Add a group")

    def addUser():
        # delete content of displayLabel
        resultDisplay.config(text="")

        # retrieve data from form
        cn = inputCn.get()
        description = inputDescription.get()

        if ((cn != "") and (description !="")):

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

        resultDisplay.config(text=connection.result['description'])
        print(connection.result['description'])
      

    # main title
    title = tk.Label(root, text="Add a user", font=("Raleway", 30))
    title.pack()

    # instructions
    instructions = tk.Label(root, text="Fill the form then press the button", font=("Raleway", 22))
    instructions.pack()

    # form
    # form cn part
    cnLabel = tk.Label(root, text="cn :")
    cnLabel.pack()
    inputCn = tk.Entry(root, width=40)
    inputCn.pack(pady=20)


    # form description part
    inputDescriptionLabel = tk.Label(root, text="description :")
    inputDescriptionLabel.pack()
    inputDescription = tk.Entry(root, width=40)
    inputDescription.pack(pady=20)

    # "add a group" button
    add_group_button = tk.Button(root, text="Add user", font="Raleway",
                                 command=addAGroup,
                                 bg="#20bebe", fg="white", height=2, width=10)

    add_group_button.pack()


    # result display
    resultDisplay = tk.Label(root, text="", font=("Raleway", 22))
    resultDisplay.pack()

    root.mainloop()

