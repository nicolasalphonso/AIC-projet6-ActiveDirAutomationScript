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
    # Search base to search for.
    search_base = 'dc=asertech,dc=fr'
    # search filter
    search_filter = '(objectClass=user)'


    try:
        # specified attributes will be returned
        connection.search(search_base=search_base,
                         search_filter=search_filter,
                         search_scope=SUBTREE,
                         attributes=['cn', 'sn', 'uid', 'uidNumber'])
        # results will take the results of search
        results = connection.response

    except LDAPException as e:
        results = e

    print(results)