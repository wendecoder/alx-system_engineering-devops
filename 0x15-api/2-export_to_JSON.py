#!/usr/bin/python3
"""Returns copleted todos for a given employee ID."""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "todos", params={"userId": id}).json()
    users = requests.get(url + "users/{}".format(id)).json()

    with open("{}.json".format(id), "w") as filejson:
        json.dump({id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": users.get("username")
            } for t in user]}, filejson)
