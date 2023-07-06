#!/usr/bin/python3
"""python script that returns the information about employee's TODOlist progresss"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/{}/'
    employee_request = requests.get(url.format(argv[1]))
    """convert the employee's response from json to python's dictionary"""
    employee_json_data = json.loads(employee_request.text)
    """extract employee name"""
    employee_name = employee_json_data.get("name")
    """requesting employee's TODO list"""
    request_todolist = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks = {}
    employeetodo_list = json.loads(request_todolist)
    """looping through todo list"""
    for list in employeetodo_list:
        tasks.update({list.get("title"): list.get("completed")})
        """returning the name and total number of the tasks"""
    EMPLOYEE_NAME = employee_name
    NUMBER_OF_DONE_TASKS = len(tasks)
    TOTAL_NUMBER_OF_TASKS = len([z for z,n in tasks.items() if n is True])
    print("employee {} is done with tasks({}/{})".format(EMPLOYEE_NAME,NUMBER_OF_DONE_TASKS,TOTAL_NUMBER_OF_TASKS))
    for z ,n in tasks.items():
        if n is True:
            print("\t {}".format(z))
