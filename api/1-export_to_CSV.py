#!/usr/bin/python3
import urllib.request
import json
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    with urllib.request.urlopen(user_url) as user_response:
        user_info = json.loads(user_response.read().decode())

    with urllib.request.urlopen(todos_url) as todos_response:
        todos_info = json.loads(todos_response.read().decode())

    employee_name = user_info["name"]
    employee_username = user_info["username"]
    task_completed = list(filter(lambda obj: obj["completed"], todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    with open(str(id) + '.csv', "w") as file:
        for task in todos_info:
            file.write(
                '"' + str(id) + '",' +
                '"' + employee_username + '",' +
                '"' + str(task["completed"]) + '",' +
                '"' + task["title"] + '",' + "\n"
            )
