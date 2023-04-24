#!/usr/bin/python3
"""This script returns an employee's id and informations about the progress
f his/her TODO list
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
            users.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
