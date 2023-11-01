#!/usr/bin/python3
"""Module"""

import requests
import sys

"""Module"""

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj: obj["completed"], todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in task_completed:
        print(f"\t {task['title']}")