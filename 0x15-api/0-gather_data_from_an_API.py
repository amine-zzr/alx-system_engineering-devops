#!/usr/bin/python3
''' This module uses a REST API to process data '''

import requests
import sys


def get_employee_todo_progress(employee_id):
    ''' get the employee data '''
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch the employee details
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()

    # Fetch the employee's tasks
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)

    # Display the result
    print(f"Employee {employee_name} is done with \
tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
