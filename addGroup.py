import os
import menu  # import of menu module
from ldap3 import *
from dotenv import load_dotenv  # use of python-dotenv to hide credentials and use environment variables
load_dotenv()
from ldap3.core.exceptions import LDAPException, LDAPBindError

def display(connection):
    dl_shortname = 'DL_EXAMPLE_SECGROUP'
    dl_group_dn = 'CN='+ dl_shortname + ',DC=asertech,DC=fr'
    object_class = 'group'
    attr = {
        'cn': dl_shortname,
        'description': 'This is a dummy description',
        'groupType':'-2147483644',
        'sAMAccountName': dl_shortname
    }

    connection.add(dl_group_dn, object_class, attr)

    print(connection.result['description'])