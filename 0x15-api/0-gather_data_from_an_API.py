#!/usr/bin/python3
"""
Python script that, using REST API (https://jsonplaceholder.typicode.com/), for
a given employee ID, returns information about his/her TODO list progress.
"""
import urllib
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]

    if len(sys.argv) < 2 or type(sys.argv[1]) != int:
        print('Usage: 0-gather_data_from_an_API.py <int>')
        return

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
