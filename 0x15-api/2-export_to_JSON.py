#!/usr/bin/python3
"""Module for exporting data into a json """
import json
import requests
import sys


def main():
    """
    main function for utilizing REST api
    exporting data to a json file
    """
    emp_id = sys.argv[1]
    id_url = 'https://jsonplaceholder.typicode.com/users/' + emp_id
    r_name = requests.get(id_url)
    if r_name.status_code == 200:
        data_queries = {sys.argv[1]: []}
        user_name = r_name.json().get("username")
        todo_url = 'https://jsonplaceholder.typicode.com/todos'
        r_task = requests.get(todo_url)
        filename = emp_id + '.json'
    for item in r_task.json():
        if item.get("userId") == int(sys.argv[1]):
            data = {'task': item.get('title'),
                    'completed': item.get('completed'),
                    'username': user_name}
            data_queries[sys.argv[1]].append(data)
    with open(filename, 'w') as f:
        json.dump(data_queries, f)


if __name__ == "__main__":
    main()
