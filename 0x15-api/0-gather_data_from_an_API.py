#!/usr/bin/python3
"""
Python script that, using REST API (https://jsonplaceholder.typicode.com/), for
a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        user = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + user
        repos = requests.get(url)
        name = repos.json().get("name")

        url = "https://jsonplaceholder.typicode.com/users/" + user + "/todos"
        repos = requests.get(url)
        done = len([todo for todo in repos.json() if todo.get("completed")])
        total = len(repos.json())

        first = True
        for element in repos.json():
            if first:
                print("Employee {} is done with tasks({}/{}):".
                      format(name, done, total))
                first = False
            if element.get("completed"):
                print("\t {}".format(element.get("title")))
