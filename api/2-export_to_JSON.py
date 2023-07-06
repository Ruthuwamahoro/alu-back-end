#!/usr/bin/python3
import urllib.request
import json
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)

    with urllib.request.urlopen(user_url) as user_response:
        user_data = user_response.read().decode()
        user_info = json.loads(user_data)

    with urllib.request.urlopen(todos_url) as todos_response:
        todos_data = todos_response.read().decode()
        todos_info = json.loads(todos_data)

    employee_username = user_info["username"]

    todos_info_sorted = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_username
        }
        for task in todos_info
    ]

    user_dict = {str(employee_id): todos_info_sorted}
    with open(str(employee_id) + '.json', "w") as file:
        file.write(json.dumps(user_dict))
