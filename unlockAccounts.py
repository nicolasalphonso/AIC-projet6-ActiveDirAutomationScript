import os
import time

from ldap3 import SUBTREE, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

import logsManagement


def unlock_accounts(connection):
    # determine a good time based complement for the log filename
    initial_time = time.strftime("%Y%m%d-%H%M%S")

    # define the first line of the log file
    initial_log = "Logs: Unlock accounts - " + initial_time
    logs = initial_log

    # define search filter and search base
    search_filter = "(&(objectClass=user)(lockoutTime>=1))"

    search_base = os.environ.get("SEARCHBASE")

    # search for all locked accounts
    try:
        connection.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn'])

    except LDAPException as e:
        logs += "\n Error : " + str(e)

    # unlock each locked account
    for element in connection.response:
        try:
            user_dn = element["dn"]
            print("locked user : " + user_dn)
            logs += "\n Locked user : " + user_dn

            # unlock user setting lockoutTime to 0
            try:
                connection.modify(user_dn, {'lockoutTime': [(MODIFY_REPLACE, ['0'])]})
                logs += "\n unlocked"

            except LDAPException as e:
                logs += "\n Error : " + str(e)

        except Exception:
            pass

    # print and write logs
    logsManagement.write_logs(logs, initial_log, initial_time, "unlock_accounts")
