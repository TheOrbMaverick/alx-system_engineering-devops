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


    todos = response.json()
    if not todos:
        print("No data available for employee ID")
  
    
    for id in todos:
        employeeID = id["userId"]

        userUrl = "https://jsonplaceholder.typicode.com/users?id={}".format(
        employeeID
        )

        nameResponse = requests.get(userUrl)
        name = nameResponse.json()
        employee_name = name[employeeID]["username"]

        output_data = {str(employeeID):[]}
        for todo in todos:
            task_completed_status = todo['completed']
            output_data[str(employeeID)].append({
                "task": todo['title'],
                "completed": task_completed_status,
                "username": employee_name
            })
            output_file = "todo_all_employees.json"
            with open(output_file, "w") as file:
                json.dump(output_data, file, indent=4)
