FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(f"{filepath}", 'r') as file:
        todos_local = file.readlines()
    return todos_local


def set_todos(todos, filepath=FILEPATH):
    with open(f'{filepath}', 'w') as file:
        file.writelines(todos)

