from tkinter import filedialog
from datetime import datetime
from ldap3.core.exceptions import LDAPException
from ldap3 import MODIFY_REPLACE
import csv
import os


def upload_action(connection):
    initial_log = "Logs: Create Users form CSV"+str(datetime.now())
    logs = initial_log

    filename = filedialog.askopenfilename()

    data = open(filename, encoding="utf-8")

    print('Selected:', filename)

    csv_data = csv.reader(data)

    data_lines = list(csv_data)

    for line in data_lines[1:]:
        firstname = line[0]
        lastname = line[1]
        address = line[2]
        phone = line[3]
        ou = line[4]
        sam_account_name = (firstname + lastname).lower()
        display_name = firstname + " " + lastname
        temp_password = os.environ.get("TEMPUSERSPASSWORD")
        user_dn = 'cn=' + sam_account_name + ',ou=' + ou + os.environ.get("SEARCHDC")

        try:
            # check if the Organisational Unit needs to be created
            # first check it does not exist
            ou_dn = 'ou=' + ou + os.environ.get("SEARCHDC")
            if not connection.search(ou_dn, '(objectClass=OrganizationalUnit)'):
                logs += "\n Error : Organisational Unit " + ou + " doesn't exist"
                try:
                    connection.add(ou_dn,
                                   attributes={'objectClass': ['OrganizationalUnit']})
                    logs += "\n Organisational Unit " + ou + " created successfully"
                except LDAPException as e:
                    logs += "\n Error : " + str(e)

            # Create users
            try:
                connection.add(user_dn,
                               attributes={'objectClass': ['user'],
                                           'samAccountName': sam_account_name,
                                           'UserPrincipalName': "{}@{}".format(sam_account_name,
                                                                               os.environ.get("DOMAIN")),
                                           'department': ou,
                                           'streetAddress': address,
                                           'telephoneNumber': phone,
                                           'company': os.environ.get("COMPANY"),
                                           'givenName': firstname,
                                           'sn': lastname,
                                           'displayName': display_name,
                                           # 'userAccountControl': ['544'],
                                           })

                # set password to temporary password
                try:
                    # works only with tls connection
                    # connection.modify(user_dn, {'userPassword':[(MODIFY_REPLACE, temp_password)]})
                    connection.extend.microsoft.modify_password(user_dn, new_password=temp_password, old_password=None)
                    connection.modify(user_dn, {'userAccountControl': [(MODIFY_REPLACE, 544)]})
                    print("Active Directory password was set successfully!")
                except LDAPException as e:
                    logs += "\n Error : " + str(e)

            except LDAPException as e:
                logs += "\n Error : " + str(e)
        except LDAPException as e:
            logs += "\n Error : " + str(e)

    if logs == initial_log:
        logs += "\n Nothing to declare ! :)"
    print(logs)
