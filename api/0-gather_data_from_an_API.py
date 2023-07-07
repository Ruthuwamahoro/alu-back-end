#!/usr/bin/python3
"""python script that returns the value of employee TODOlist"""
import json
import sys
import urllib.request
"""module"""
if __main__ == '__name__' :
    """converting the arguments into integers"""
    user_id = int(sys.argv[1])
    """using url to retrieve a data about employees"""
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{user_id}"
    todo_url = f"{base_url}/todos?userId={user_id}"
    """open employee url using urllib module"""
    with urllib.request.urlopen(employee_url) as f:
        employee_info = json.load(f)
    with urllib.request.urlopen(todo_url) as response:
        data = json.load(response)
    """retieving a data about employee name,task completed and total number of tasks"""
    EMPLOYEE_NAME = employee_info["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = [task for task in data if task["completed"]]


    print(f"Employee {EMPLOYEE_NAME} is done with tasks({len(NUMBER_OF_DONE_TASKS)}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in NUMBER_OF_DONE_TASKS:
        print(f"\t{task['title']}")
