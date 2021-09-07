from ldap3 import SUBTREE, MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException
import os
import time


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

            # unlock user setting lockoutTime to 0
            try:
                connection.modify(user_dn, {'lockoutTime': [(MODIFY_REPLACE, ['0'])]})
                print("ok")

            except LDAPException as e:
                logs += "\n Error : " + str(e)

        except Exception:
            pass

    # if no log was written, just add "Nothing to declare" in the log file
    if logs == initial_log:
        logs += "\n Nothing to declare ! :)"
    print(logs)

    # create the logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # create the log file in logs folder
    log_file_name = "logs/unlock_accounts_" + initial_time + ".txt"
    file = open(log_file_name, "a")
    file.write(logs)
    file.close()
