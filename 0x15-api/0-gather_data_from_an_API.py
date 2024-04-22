#!/usr/bin/python3
""" Gather data from an API """

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employeeID = sys.argv[1]

    if not employeeID.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employeeID)
    userUrl = "https://jsonplaceholder.typicode.com/users?id={}".format(employeeID)
    nameResponse = requests.get(userUrl, verify=False)
    name = nameResponse.json()
    employee_name = name[0]["username"]

    response = requests.get(url, verify=False)
    if response.status_code != 200:
        print("Error: Unable to fetch data from API")
        sys.exit(1)
    
    todos = response.json()
    if not todos:
        print("No data available for employee ID:", employeeID)
        sys.exit(1)
    
    completed_tasks = 0
    total_tasks = len(todos)

    for todo in todos:
        if todo.get('completed', False):
            completed_tasks += 1

    print("Employee {} is done with tasks({}/{})".format(employee_name, completed_tasks, total_tasks))
    for todo in todos:
        if todo.get('completed', False):
            print("\t{}".format(todo['title']))