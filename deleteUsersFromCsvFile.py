import os
import time

from ldap3.core.exceptions import LDAPException

import csvFileManagement
import logsManagement


def upload_action(connection):
    # determine a good time based complement for the log filename
    initial_time = time.strftime("%Y%m%d-%H%M%S")

    # define the first line of the log file
    initial_log = "Logs: Delete Users form CSV" + initial_time
    logs = initial_log

    # open csv file
    data_lines = csvFileManagement.open_csv_file()

    # for each line, retrieve necessary elements
    for line in data_lines[1:]:
        sam_account_name = line[0]
        ou = line[1]
        user_dn = 'cn=' + sam_account_name + ',ou=' + ou + os.environ.get("SEARCHDC")

        # Delete users
        try:
            connection.delete(user_dn)
            logs += "\n User deleted : " + user_dn

        except LDAPException as e:
            logs += "\n Error : " + str(e)

    # print and write logs
    logsManagement.write_logs(logs, initial_log, initial_time, "delete_users")
