#!/usr/bin/python3
import urllib.request
import json
from sys import argv


if __name__ == "__main__":
    """
        request user info by employee ID
    """
    request_employee = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    """
        convert response to string and load as JSON
    """
    employee_data = request_employee.read().decode()
    employee = json.loads(employee_data)
    """
        extract employee name
    """
    employee_name = employee.get("name")

    """
        request user's TODO list
    """
    request_todos = urllib.request.urlopen('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    """
        convert response to string and load as JSON
    """
    todos_data = request_todos.read().decode()
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
