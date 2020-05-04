#!/usr/bin/python3
"""
Python script that, using REST API (https://jsonplaceholder.typicode.com/), for
a given employee ID, returns information about is/her TODO list progress but
store it in a CSV file.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        user = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + user
        repos = requests.get(url)
        username = repos.json().get("username")

        url = "https://jsonplaceholder.typicode.com/users/" + user + "/todos"
        repos = requests.get(url)

        for element in repos.json():
            print('"{}","{}","{}","{}"'.format(user, username,
                                               element.get("completed"),
                                               element.get("title")))
