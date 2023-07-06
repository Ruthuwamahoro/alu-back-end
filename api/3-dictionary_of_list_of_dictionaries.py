#!/usr/bin/python3
"""python script to records all tasks from all employees"""
import urllib.request
import json


def get_employee_task(employee_id):
    """Doc"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

    with urllib.request.urlopen(user_url) as user_response:
        user_data = user_response.read().decode()
        user_info = json.loads(user_data)

    employee_username = user_info["username"]
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    with urllib.request.urlopen(todos_url) as todos_response:
        todos_data = todos_response.read().decode()
        todos_info = json.loads(todos_data)

    return [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_username
        }
        for task in todos_info
    ]


def get_employee_ids():
    """Doc"""
    users_url = "https://jsonplaceholder.typicode.com/users/"

    with urllib.request.urlopen(users_url) as users_response:
        users_data = users_response.read().decode()
        users_info = json.loads(users_data)

    ids = list(map(lambda user: user["id"], users_info))
    return ids


if __name__ == '__main__':
    employee_ids = get_employee_ids()

    with open('todo_all_employees.json', "w") as file:
        all_users = {}
        for employee_id in employee_ids:
            all_users[str(employee_id)] = get_employee_task(employee_id)
        file.write(json.dumps(all_users))
