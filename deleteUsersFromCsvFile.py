from datetime import datetime
from tkinter import filedialog
from ldap3.core.exceptions import LDAPException
import csv
import os


def upload_action(connection):
    initial_log = "Logs: Delete Users form CSV"+str(datetime.now())
    logs = initial_log

    filename = filedialog.askopenfilename()

    data = open(filename, encoding="utf-8")

    print('Selected:', filename)

    csv_data = csv.reader(data)

    data_lines = list(csv_data)

    for line in data_lines[1:]:
        sam_account_name = line[0]
        ou = line[1]
        user_dn = 'cn=' + sam_account_name + ',ou=' + ou + os.environ.get("SEARCHDC")

        # Delete users
        try:
            connection.delete(user_dn)

        except LDAPException as e:
            logs += "\n Error : " + str(e)

    if logs == initial_log:
        logs += "\n Nothing to declare ! :)"
    print(logs)
