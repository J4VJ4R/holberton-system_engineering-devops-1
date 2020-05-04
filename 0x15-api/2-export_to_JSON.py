#!/usr/bin/python3
"""
Python script that, using REST API (https://jsonplaceholder.typicode.com/), for
a given employee ID, returns information about his/her TODO list progress and
save it in a JSON file.
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

        cu = ""
        for element in repos.json():
            s = '"task": "{}", "completed": "{}", "username": "{}"'.format(
                element.get("title"),
                element.get("completed"),
                username)
            if cu == "":
                sep = ""
            else:
                sep = ", "
            cu = cu + sep + "{" + s + "}"
        cu = '"{}": [{}]'.format(user, cu)
        cu = '{' + cu + '}'
        print(cu)

        with open('{}.json'.format(user), 'w') as the_file:
            the_file.write("{}\n".format(cu))
