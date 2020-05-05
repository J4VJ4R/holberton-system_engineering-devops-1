#!/usr/bin/python3
"""
Python script that, using REST API (https://jsonplaceholder.typicode.com/), for
a given employee ID, returns information about his/her TODO list progress and
save it in a JSON file.
"""


if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) >= 2 and sys.argv[1].isdigit():
        user = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + user
        repos = requests.get(url)
        username = repos.json().get("username")

        url = "https://jsonplaceholder.typicode.com/users/" + user + "/todos"
        repos = requests.get(url)

        todo = {}
        cu = []
        for element in repos.json():
            s = {"task": element.get('title'),
                 "completed": element.get('completed'),
                 "username": username}
            cu.append(s)
        todo[user] = cu

        with open('{}.json'.format(user), 'w') as the_file:
            json.dump(todo, the_file)
