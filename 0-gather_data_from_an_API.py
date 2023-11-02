#!/usr/bin/python3
"""
Script that uses REST API that returns the
information about the status of an employee's TODO list given an employee ID.
Usage: 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys

if __name__ == "__main":
    if len(sys.argv) != 2:
        sys.exit("Usage: 0-gather_data_from_an_API.py <employee_id>")

    emp_id = sys.argv[1]
    if not emp_id.isdigit():
        sys.exit("Employee ID must be an integer.")

    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": emp_id})
        response.raise_for_status()  # Check for request errors
        tasks = response.json()

        employee = requests.get(f"https://jsonplaceholder.typicode.com/users/{emp_id}")
        employee.raise_for_status()  # Check for request errors
        emp_name = employee.json().get('name')

        completed = sum(1 for task in tasks if task.get('completed'))

        print(f"Employee {emp_name} is done with tasks ({completed}/{len(tasks)}):")
        for task in tasks:
            if task.get('completed'):
                print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        sys.exit(f"An error occurred during the API request: {e}")
