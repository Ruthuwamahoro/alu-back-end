#!/usr/bin/python3
"""Python script that returns the employee's TODOlist"""
import requests
from sys import argv

if __name__ == '__main__':
    employee_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(argv[1])
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(argv[1])

    employee_request = requests.request('GET', employee_url).json()
    employee_todos = requests.request('GET' , todos_url).json()
    employee_name = employee_request["name"]
    tasks_completed = list(filter(lambda obj: (obj["completed"] is True),employee_todos))
    EMPLOYEE_NAME = employee_name
    NUMBER_OF_DONE_TASKS = len(tasks_completed)
    TOTAL_NUMBER_OF_TASKS = len(employee_todos)
    print("Employee {} is done with tasks({}/{}):".
          format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    [print("\t " + task["title"]) for task in tasks_completed]
