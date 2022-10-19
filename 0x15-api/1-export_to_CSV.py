#!/usr/bin/python3
"""Returns copleted todos for a given employee ID."""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    username = requests.get(url + "users/{}".format(sys.argv[1])).json()
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as filecsv:
        write = csv.writer(filecsv, quoting=csv.QUOTE_ALL)
        [write.writerow(
            [sys.argv[1], username.get("username"), t.get("completed"), t.get("title")]
         ) for t in user]
