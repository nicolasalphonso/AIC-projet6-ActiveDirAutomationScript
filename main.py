from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

from ldap3 import Server, Connection, SAFE_SYNC

print("Hello World")