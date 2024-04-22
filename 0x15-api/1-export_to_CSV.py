#!/usr/bin/python3
""" Gather data from an API """

import csv
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
    employee_name = name[0]["name"]

    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from API")
        return

    todos = response.json()
    if not todos:
        print("No data available for employee ID:", employeeID)
        return

    completed_tasks = 0
    total_tasks = len(todos)

    completed_task_titles = []
    for todo in todos:
        if todo['completed']:
            completed_tasks += 1
            completed_task_titles.append(todo['title'])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks
        ))
    for title in completed_task_titles:
        print("\t {}".format(title))

    output_filename = "{}.csv".format(employeeID)
    with open(output_filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )
        for todo in todos:
            task_completed_status = "True" if todo['completed'] else "False"
            writer.writerow([
                employeeID, employee_name, task_completed_status, todo['title']
                ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employeeID = sys.argv[1]

    if not employeeID.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    employee_todo(int(employeeID))
