#!/usr/bin/python3
"""module"""
import json
from sys import argv
import urllib.request
if __name__ == "__main__":
    """
        request user info by employee ID
    """
    employee_url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1])
    with urllib.request.urlopen(employee_url) as employee_response:
        employee_data = employee_response.read().decode()
        employee = json.loads(employee_data)
        """
            extract employee name
        """
        employee_name = employee.get("name")

    """
        request user's TODO list
    """
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1])
    with urllib.request.urlopen(todos_url) as todos_response:
        todos_data = todos_response.read().decode()
        employee_todos = json.loads(todos_data)
        """
            dictionary to store task status in boolean format
        """
        tasks = {}
        """
            loop through dictionary & get completed tasks
        """
        for dictionary in employee_todos:
            tasks.update({dictionary.get("title"): dictionary.get("completed")})

    """
        return name, total number of tasks & completed tasks
    """
    EMPLOYEE_NAME = employee_name
    TOTAL_NUMBER_OF_TASKS = len(tasks)
    NUMBER_OF_DONE_TASKS = len([k for k, v in tasks.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for k, v in tasks.items():
        if v is True:
            print("\t {}".format(k))
