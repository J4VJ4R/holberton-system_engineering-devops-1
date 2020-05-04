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
        url = "https://jsonplaceholder.typicode.com/user/" + user + "/todos"
        repos = requests.get(url)

        first = True
        done = len([todo for todo in repos.json() if todo.get("completed")])
        total = len(repos.json())

        for element in repos.json():
            if first:
                print("Employee Ervin Howell is done with tasks({}/{}):".
                    format(done, total))
                first = False
            if element.get("completed"):
                print("\t {}".format(element.get("title")))
