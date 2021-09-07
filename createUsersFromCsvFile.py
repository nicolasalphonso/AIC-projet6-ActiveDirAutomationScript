import os
import time

from ldap3 import MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

import csvFileManagement
import logsManagement

'''
this function creates Active Directory users according to a CSV file chosen by the user
'''


def upload_action(connection):
    # determine a good time based complement for the log filename
    initial_time = time.strftime("%Y%m%d-%H%M%S")

    # define the first line of the log file
    initial_log = "Logs: Create Users form CSV" + initial_time
    logs = initial_log

    # open csv file
    data_lines = csvFileManagement.open_csv_file()

    # for each line, retrieve necessary elements
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
                                           })

                # N.B.: works only with ssl connection
                try:
                    # set password to temporary password
                    connection.extend.microsoft.modify_password(user_dn, new_password=temp_password, old_password=None)

                    # force user to change password on next connection
                    connection.modify(user_dn, {'pwdLastSet': [(MODIFY_REPLACE, [0])]})

                    # userAccountControl : 512 - normal account
                    connection.modify(user_dn, {'userAccountControl': [(MODIFY_REPLACE, '512')]})

                    # add result to logs
                    logs += "\n User added : " + user_dn

                except LDAPException as e:
                    logs += "\n Error : " + str(e)

            except LDAPException as e:
                logs += "\n Error : " + str(e)

        except LDAPException as e:
            logs += "\n Error : " + str(e)

    # print and write logs
    logsManagement.write_logs(logs, initial_log, initial_time, "add_users")
