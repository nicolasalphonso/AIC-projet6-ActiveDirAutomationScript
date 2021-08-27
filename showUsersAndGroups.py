import os
import menu  # import of menu module
from ldap3 import Server, Connection, SAFE_SYNC, SUBTREE
from dotenv import load_dotenv  # use of python-dotenv to hide credentials and use environment variables
load_dotenv()
from ldap3.core.exceptions import LDAPException, LDAPBindError

'''
def display(connection):
    connection.add('cn=user1,ou=users,o=asertech', ['inetOrgPerson', 'posixGroup', 'top'], {'sn': 'user_sn', 'gidNumber': 0})
    print("add user")
'''

def display(connection):
    # Provide a search base to search for.
    search_base = 'dc=asertech,dc=fr'
    # provide a uidNumber to search for. '*" to fetch all users/groups
    search_filter = '(objectClass=user)'


    try:
        # only the attributes specified will be returned
        connection.search(search_base=search_base,
                         search_filter=search_filter,
                         search_scope=SUBTREE,
                         attributes=['cn', 'sn', 'uid', 'uidNumber'])
        # search will not return any values.
        # the entries method in connection object returns the results
        results = connection.response
    except LDAPException as e:
        results = e

    print(results)