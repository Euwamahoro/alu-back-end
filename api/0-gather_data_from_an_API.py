#!/usr/bin/python3

import requests

def get_todo_list_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the list of TODO items from the response
        todo_list = response.json()

        # Count the number of completed and incomplete TODO items
        completed_count = sum(1 for todo in todo_list if todo['completed'])
        incomplete_count = len(todo_list) - completed_count

        # Print the TODO list progress
        print(f"Employee ID: {employee_id}")
        print(f"Completed TODO items: {completed_count}")
        print(f"Incomplete TODO items: {incomplete_count}")
    else:
        print(f"Failed to fetch TODO list for employee ID: {employee_id}")

# Example usage
employee_id = 1
get_todo_list_progress(employee_id)