#!/usr/bin/python3
''' This module uses a REST API to process data '''
import json
import requests


def fetch_data():
    '''Fetch user data'''
    # Define the base URL for the API
    base_url = 'https://jsonplaceholder.typicode.com'

    users_response = requests.get(f'{base_url}/users')
    users = users_response.json()

    # Fetch tasks data
    tasks_response = requests.get(f'{base_url}/todos')
    tasks = tasks_response.json()

    return users, tasks


def process_data(users, tasks):
    '''Initialize the dictionary to hold all tasks for each user'''
    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        # List to hold task details for the current user
        user_tasks = []

        for task in tasks:
            if task['userId'] == user_id:
                task_info = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                }
                user_tasks.append(task_info)

        # Add the user's tasks to the all_tasks dictionary
        all_tasks[user_id] = user_tasks

    return all_tasks


def export_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    # Fetch data from the API
    users, tasks = fetch_data()

    # Process data to the required format
    all_tasks = process_data(users, tasks)

    # Export data to JSON file
    export_to_json(all_tasks, 'todo_all_employees.json')
