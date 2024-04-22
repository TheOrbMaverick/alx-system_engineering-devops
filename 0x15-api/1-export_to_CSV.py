#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys


def employee_todo(employeeID):
    """Retrieve employee TODO list progress from API"""
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employeeID
        )

    userUrl = "https://jsonplaceholder.typicode.com/users?id={}".format(
        employeeID
        )
    nameResponse = requests.get(userUrl)
    name = nameResponse.json()
    employee_name = name[0]["username"]

    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from API")
        return

    todos = response.json()
    if not todos:
        print("No data available for employee ID:", employeeID)
        return

    output_file = "{}.csv".format(employeeID)
    with open(output_file, "w", newline="") as file:
        for todo in todos:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeID, employee_name, todo['completed'], todo['title']
                ))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employeeID = sys.argv[1]

    if not employeeID.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    employee_todo(int(employeeID))
