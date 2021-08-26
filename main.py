import os

from dotenv import load_dotenv # use of python-dotenv to hide credentials and use environment variables
load_dotenv()  # take environment variables from .env

from ldap3 import Server, Connection, SAFE_SYNC

print(os.environ.get("ESSAI"))