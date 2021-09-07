from ldap3 import SUBTREE, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException
import os
from datetime import datetime


def unlock_accounts(connection):
    initial_log = "Logs: Unlock accounts" + str(datetime.now())
    logs = initial_log

    search_filter = "(&(objectClass=user)(lockoutTime>=1))"

    search_base = os.environ.get("SEARCHBASE")

    try:
        connection.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn'])

    except LDAPException as e:
        logs += "\n Error : " + str(e)

    for element in connection.response:
        try:
            user_dn = element["dn"]
            print(user_dn)

            # unlock user
            try:
                connection.modify(user_dn, {'lockoutTime': [(MODIFY_REPLACE, ['0'])]})
                print("ok")
            except LDAPException as e:
                logs += "\n Error : " + str(e)
        except:
            pass

    if logs == initial_log:
        logs += "\n Nothing to declare ! :)"

    print(logs)
