#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import menu  # import of menu module
from ldap3 import Server, Connection, SAFE_SYNC
from dotenv import load_dotenv  # use of python-dotenv to hide credentials and use environment variables
load_dotenv()  # take environment variables from .env

# defining server and connexion variables from .env file information
serverAddress = os.environ.get("SERVER")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")

# connection to LDAP server
server = Server(host=serverAddress)
# connection = Connection(server, user, password, client_strategy=SAFE_SYNC, auto_bind=True)
connection = Connection(server, auto_bind=True)

# verifying connection for development purpose
print(connection)

# Main menu
menu.display()
