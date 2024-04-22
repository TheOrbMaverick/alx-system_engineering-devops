#!/usr/bin/python3
""" Gather data from an API """

import json
import requests
import sys


if __name__ == "__main__":
    """Retrieve employee TODO list progress from API"""

    url = "https://jsonplaceholder.typicode.com/todos"

    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from API")
        sys.exit(1)

    todos = response.json()
    if not todos:
        print("No data available for employee ID")
        sys.exit(1)

    # Dictionary to store todo data for each employee
    all_employee_data = {}

    for todo in todos:
        employeeID = todo["userId"]

        # Retrieve user information for the employee
        userUrl = f"https://jsonplaceholder.typicode.com/users/{employeeID}"
        nameResponse = requests.get(userUrl)
        name = nameResponse.json()
        employee_name = name["username"]

        # Prepare todo data for the current employee
        task_completed_status = todo['completed']
        todo_data = {
            "username": employee_name,
            "task": todo['title'],
            "completed": task_completed_status
        }

        # Add todo data to the list of todos for this employee
        if employeeID not in all_employee_data:
            all_employee_data[employeeID] = []
        all_employee_data[employeeID].append(todo_data)

    # Write all employee data to a single JSON file
    output_file = "todo_all_employees.json"
    with open(output_file, "w") as file:
        json.dump(all_employee_data, file, indent=4)
