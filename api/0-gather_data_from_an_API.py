#!/usr/bin/python3
'''get info from api'''

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    userId = argv[1]

    user = requests.get(url + "users/{}".format(userId)).json()
    todos = requests.get(url + "todos?userId={}".format(userId)).json()

    name = user.get("name")
    ct = 0
    t = len(todos)
    tasks = ""

    for todo in todos:
        if todo.get("completed"):
            ct += 1
            title = todo.get("title")
            tasks += "\t {}\n".format(title)

            line = "Employee {} is done with tasks({}/{})".format(name, ct, t)

    print(line)
    print(tasks, end="")
