import os
import time

from ldap3 import MODIFY_REPLACE
from ldap3.core.exceptions import LDAPException

import csvFileManagement
import logsManagement


def upload_action(connection):
    # determine a good time based complement for the log filename
    initial_time = time.strftime("%Y%m%d-%H%M%S")

    # define the first line of the log file
    initial_log = "Logs: Activate Users form CSV" + time.strftime("%Y%m%d-%H%M%S")
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
            # userAccountControl : 512 - Enable Account
            connection.modify(user_dn, {'userAccountControl': [(MODIFY_REPLACE, ['512'])]})
            logs += "\n User activated : " + user_dn

        except LDAPException as e:
            logs += "\n Error : " + str(e)

    # print and write logs
    logsManagement.write_logs(logs, initial_log, initial_time, "activate_users")
