import functions_app1
import time

date = time.strftime("%d %B , %Y %H:%M:%S")
print("This is ", date)
while True:
    user_input = input("Enter add , show ,complete, edit or exit : ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        todos = functions_app1.get_todos()
        todo = user_input[4:]
        todos.append(todo + "\n")
        functions_app1.write_todos(todos)

    elif user_input.startswith("show"):
        todos = functions_app1.get_todos()
        for index, items in enumerate(todos):
            print(f"{index + 1}-{items}", end="")

    elif user_input.startswith("exit"):
        break

    elif user_input.startswith("edit"):
        try:
            todos = functions_app1.get_todos()
            num = int(user_input[5:])
            num = num - 1
            new_todo = input("Enter the todo : ") + "\n"
            todos[num] = new_todo
            functions_app1.write_todos(todos)
        except ValueError:
            print("Please enter a valid command !")
            continue

    elif user_input.startswith("complete"):
        try:
            todos = functions_app1.get_todos("file_app1")
            num = int(user_input[9:])
            todo_remove = todos.pop(num - 1)
            todo_remove = todo_remove.strip("\n")
            print(f"{todo_remove} is removed from the todo-list")
            functions_app1.write_todos(todos)
        except IndexError:
            print("There is no item in this number !")
            continue

    else:
        print("Enter only add,show or exit !")
print("Thank you for using my page!!")
