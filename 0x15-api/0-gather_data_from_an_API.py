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

    # output_filename = "employee_todo_{}.txt".format(employeeID)
    # with open(output_filename, "w") as file:
    #     file.write("Employee {} is done with tasks({}/{}):\n".format(
    #         employee_name, completed_tasks, total_tasks
    #         ))
    #     for title in completed_task_titles:
    #         file.write("\t{}\n".format(title))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employeeID = sys.argv[1]

    if not employeeID.isdigit():
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    employee_todo(int(employeeID))
