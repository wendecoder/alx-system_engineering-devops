#!/usr/bin/python3
"""Returns copleted todos for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = requests.get(url + "users/{}".format(sys.argv[1])).json()

    completed = [t.get("title") for t in user if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        username.get("name"), len(completed), len(user)))
    [print("\t {}".format(c)) for c in completed]
