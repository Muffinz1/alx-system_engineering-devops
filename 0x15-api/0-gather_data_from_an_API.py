#!/usr/bin/python3
""" module for requesting employer id and pw """
import requests
import sys


def main():
    """
    main function for getting the employer id and pw
    utilizing the requests liberary and REST api
    """
    task_names = []
    tasks = 0
    done = 0
    emp_id = sys.argv[1]
    id_url = 'https://jsonplaceholder.typicode.com/users/' + emp_id
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    r_name = requests.get(id_url)
    name = r_name.json().get("name")
    r_task = requests.get(todo_url)

    for item in r_task.json():
        if item.get("userId") == int(emp_id):
            tasks += 1
            if item.get("completed") is True:
                done += 1
                task_names.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name, done, tasks))
    for i in task_names:
        print("\t {}".format(i))


if __name__ == "__main__":
    main()
