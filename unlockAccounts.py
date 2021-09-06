from ldap3 import SUBTREE
from ldap3.core.exceptions import LDAPException
import os


def unlock_accounts(connect_ldap):
    search_filter = "(&(objectClass=user)(lockoutTime>=1))"

    search_base = os.environ.get("SEARCHDC")

    try:
        connect_ldap.search(search_base=search_base,
                            search_filter=search_filter,
                            search_scope=SUBTREE,
                            attributes=['cn', 'sn', 'uid', 'uidnumber'])

        results = connect_ldap.response

    except LDAPException as e:

        results = e
    print("response")
    print(connect_ldap.response)
    print("entries")
    print(connect_ldap.entries)

    return results
