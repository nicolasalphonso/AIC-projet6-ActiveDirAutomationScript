#! /usr/bin/env python3
# coding: utf-8

import os

from dotenv import load_dotenv  # use of python-dotenv to hide credentials and use environment variables
from ldap3 import Server, Connection

import menu  # import of menu module


def main():
    load_dotenv()  # take environment variables from .env

    # defining server and connexion variables from .env file information
    server_address = os.environ.get("SERVER")
    connection_user = os.environ.get("USER")
    connection_password = os.environ.get("PASSWORD")

    # connection to LDAP server
    server = Server(host=server_address, port=636, use_ssl=True)
    # connection = Connection(server, user, password, client_strategy=SAFE_SYNC, auto_bind=True)
    connection = Connection(server, user=connection_user, password=connection_password, auto_bind=True)

    # verifying connection for development purpose
    print(connection)

    # Main menu
    menu.display(connection)


if __name__ == "__main__":
    main()
