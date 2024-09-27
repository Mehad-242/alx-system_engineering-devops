#!/usr/bin/python3
import json
import requests
import sys

if name == "main":
    # Get the user ID from the command-line argument
    user_id = sys.argv[1]

    # Fetch the user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user = requests.get(user_url).json()

    # Fetch the user's tasks
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    todos = requests.get(todos_url).json()

    # Username of the user
    username = user.get('username')

    # Prepare data for the JSON file
    tasks = []
    for todo in todos:
        task_data = {
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
        }
        tasks.append(task_data)

    # Create the dictionary with the user_id as the key
    user_tasks = {user_id: tasks}

    # Write the data to a JSON file named USER_ID.json
    file_name = f"{user_id}.json"
    with open(file_name, 'w') as json_file:
        json.dump(user_tasks, json_file)
