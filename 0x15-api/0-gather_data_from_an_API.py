#!/usr/bin/python3
"""Returns copleted todos for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    user = requests.get(url, params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in user if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user[0].get("name"), len(completed), len(user)))
    [print("\t {}".format(c)) for c in completed]
