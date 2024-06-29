import functions_app1
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("file_app1.txt"):
    with open("file_app1.txt", "w") as f:
        pass

fsg.theme("DarkBlue")
clock = fsg.Text("", key="clock")
label = fsg.Text("Enter a to-do item to add : ")
input_box = fsg.InputText(tooltip="Enter todo", key="todo")
button = fsg.Button("Add")
list_box = fsg.Listbox(values=functions_app1.get_todos(), key="todos",
                       enable_events=True, size=(55, 10))
button2 = fsg.Button("Edit")
button3 = fsg.Button("Complete")
exit_button = fsg.Button("Exit")
window = fsg.Window("To-do App",
                    layout=[[clock],
                            [label, input_box, button],
                            [list_box, button2, button3],
                            [exit_button]],
                    font=("Tahoma", 16))

while True:
    action, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %B , %Y %H:%M:%S"))
    match action:
        case 'Add':
            todos = functions_app1.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions_app1.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions_app1.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions_app1.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select an item !", font=("Tahoma", 16))

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            try:
                item_to_remove = values["todos"][0]
                todos = functions_app1.get_todos()
                index = todos.index(item_to_remove)
                todos.pop(index)
                functions_app1.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                fsg.popup("Please select an item !", font=("Tahoma", 16))

        case "Exit":
            break

        case fsg.WIN_CLOSED:
            break

window.close()
