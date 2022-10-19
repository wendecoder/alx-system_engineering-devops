#!/usr/bin/python3
"""Returns copleted todos for a given employee ID."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as filejson:
        json.dump({
            c.get("id"): [{
                "username": c.get("username"),
                "task": t.get("title"),
                "completed": t.get("completed")
                } for t in requests.get(url + "todos",
                                        params={"userId": c.get("id")}).json()]
            for c in users}, filejson)
