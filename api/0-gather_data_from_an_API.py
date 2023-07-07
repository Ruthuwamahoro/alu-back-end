#!/usr/bin/python3
"""python script that returns the value of employee TODOlist"""
import json
import sys
import urllib.request
"""module"""
if __name__ == '__main__' :
    """converting the arguments into integers"""
    EMPLOYEE_ID = int(sys.argv[1])
    """using url to retrieve a data about employees"""
    BASE_URL = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(BASE_URL,EMPLOYEE_ID)
    todo_url = "{}/todos?userId={}".format(BASE_URL, EMPLOYEE_ID)
    """open employee url using urllib module"""
    with urllib.request.urlopen(employee_url) as f:
        employee_info = json.loads(f.read().decode('utf-8'))
    with urllib.request.urlopen(todo_url) as response:
        data = json.loads(response.read().decode('utf-8'))
    """retieving a data about employee name,task completed and total number of tasks"""
    EMPLOYEE_NAME = employee_info["name"]
    TOTAL_NUMBER_OF_TASKS = len(data)
    NUMBER_OF_DONE_TASKS = len([task for task in data if task["completed"]])


    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
   
    for task in data:
        if task["completed"]:
            print("\t{}".format(task["title"]))
