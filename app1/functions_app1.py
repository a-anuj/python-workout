def get_todos(filepath=r"C:\Users\Anuj\Desktop\python-20app-course\app1\file_app1"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=r"C:\Users\Anuj\Desktop\python-20app-course\app1\file_app1"):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("I have created a new python file to store all the function in my main source code ")