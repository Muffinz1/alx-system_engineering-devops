#!/usr/bin/python3
"""Module for exporting all ids data into a json """
import json
import requests


def main():
    """
    main function for utilizing REST api
    exporting all data to a json file
    """
    data_queries = {}
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    r_task = requests.get(todo_url)
    for item in r_task.json():
        if str(item.get('userId')) not in data_queries:
            data_queries[str(item.get('userId'))] = []
        id_url = 'https://jsonplaceholder.typicode.com/users?id='\
                 + str(item.get('userId'))
        id_respond = requests.get(id_url)
        json_respond = id_respond.json()
        user_name = json_respond[0]['username']
        data = {'task': item.get('title'), 'completed': item.get('completed'),
                'username': user_name}
        data_queries[str(item.get('userId'))].append(data)

    filename = 'todo_all_employees.json'
    with open(filename, 'w') as f:
        json.dump(data_queries, f)


if __name__ == "__main__":
    main()
