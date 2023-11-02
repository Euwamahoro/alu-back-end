#!/usr/bin/python3
"""
Script that uses REST API that returns the
information about the status of employee's TODO list given employee ID.
Usage: 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Please provide an employee ID")

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        sys.exit("Employee ID must be an integer.")

    response = requests.get("https://jsonplaceholder.typicode.com/todos",
                            params={"userId": emp_id})
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(emp_id))
    emp_name = employee.json().get('name')

    tasks = response.json()
    completed = 0
    for t in tasks:
        if t.get('completed'):
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, completed, len(tasks)))

    for t in tasks:
        if t.get('completed'):
            print("\t {}".format(t.get('title')))
