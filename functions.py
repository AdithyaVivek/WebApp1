import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
FilePath = "todos.txt"


def get_todos(filepath=FilePath):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def put_todos(todos_arg, filepath=FilePath):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# print(get_todos())
if __name__ == "__main__":
    print(get_todos())


# print(__name__)     # represent the todo_functions.py in other files
