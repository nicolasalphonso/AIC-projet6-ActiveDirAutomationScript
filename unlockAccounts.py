from ldap3 import Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException

def unlockAccounts(connect_ldap):
    search_filter = "(&(objectClass=user)(lockoutTime>=1))"

    search_base = 'dc=asertech,dc=fr'

    try:
        connect_ldap.search(search_base=search_base,
                          search_filter=search_filter,
                          search_scope=SUBTREE,
                          attributes=['cn', 'sn','uid','uidnumber'])

        results = connect_ldap.response

    except LDAPException as e:

        results = e
    print("response")
    print(connect_ldap.response)
    print("entries")
    print(connect_ldap.entries)

    return results