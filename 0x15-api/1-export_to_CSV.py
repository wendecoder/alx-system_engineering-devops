#!/usr/bin/python3
"""Returns copleted todos for a given employee ID."""
import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "todos", params={"userId": id}).json()
    users = requests.get(url + "users/{}".format(id)).json()
    with open("{}.csv".format(id), "w", newline="") as filecsv:
        csv = csv.writer(filecsv, quoting=csv.QUOTE_ALL)
        [csv.writerow(
            [id, users.get("username"), t.get("completed"), t.get("title")]
         ) for t in user]
