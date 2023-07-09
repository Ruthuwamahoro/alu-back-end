#!/usr/bin/python3
""" Call API and store data in CSV """
import csv
import json
import urllib.parse
import urllib.request
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos/'
    url_user = 'https://jsonplaceholder.typicode.com/users/'

    todo_params = {'userId': employee_id}
    todo_url_with_params = url_todo + '?' + urllib.parse.urlencode(todo_params)
    with urllib.request.urlopen(todo_url_with_params) as todo_response:
        todo_dict_list = json.loads(todo_response.read().decode())

    user_params = {'id': employee_id}
    user_url_with_params = url_user + '?' + urllib.parse.urlencode(user_params)
    with urllib.request.urlopen(user_url_with_params) as user_response:
        user_dict_list = json.loads(user_response.read().decode())

    employee = user_dict_list[0].get('username')

    with open("{}.csv".format(employee_id), "a+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_dict_list:
            status = task['completed']
            title = task['title']
            csvwriter.writerow([employee_id, employee, status, title])
