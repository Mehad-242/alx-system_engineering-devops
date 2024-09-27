#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
# Base URL of the API
	api_url = "https://jsonplaceholder.typicode.com/"

# Fetch employee information
	employee_url = f"{api_url}users/{employee_id}"
	employee_response = requests.get(employee_url)
	employee_data = employee_response.json()

# Fetch employee TODO list
todos_url = f"{api_url}todos?userId={employee_id}"
todos_response = requests.get(todos_url)
todos_data = todos_response.json()

# Get employee name
employee_name = employee_data.get("name")

	# Calculate total tasks and completed tasks
	total_tasks = len(todos_data)
	done_tasks = [task for task in todos_data if task.get("completed")]
	number_of_done_tasks = len(done_tasks)

# Display the progress
	print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
# Display the titles of completed tasks
	for task in done_tasks:
		print(f"\t {task.get('title')}")

if name == "main":
	if len(sys.argv) != 2:
		print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
	else:
		try:
			employee_id = int(sys.argv[1])
			get_employee_todo_progress(employee_id)
		except ValueError:
			print("Please provide a valid employee ID (integer).")
