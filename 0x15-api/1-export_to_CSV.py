#!/usr/bin/python3
"""Module for exporting data into a csv """
import csv
import requests
import sys


def main():
    """
    main function for utilizing REST api
    exporting data to a csv
    """
    emp_id = sys.argv[1]
    id_url = 'https://jsonplaceholder.typicode.com/users/' + emp_id
    r_name = requests.get(id_url)
    if r_name.status_code == 200:
        user_name = r_name.json().get("username")
        todo_url = 'https://jsonplaceholder.typicode.com/todos'
        r_task = requests.get(todo_url)
        filename = emp_id + '.csv'
    with open(filename, 'w') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
        for item in r_task.json():
            if item.get("userId") == int(emp_id):
                line = [item.get("userId"),
                        user_name,
                        str(item.get("completed")),
                        item.get('title')]
                wr.writerow(line)


if __name__ == "__main__":
    main()
