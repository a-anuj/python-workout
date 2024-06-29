import FreeSimpleGUI as fsg

fsg.theme("DarkBlue")
label1 = fsg.Text("Enter feet ")
label2 = fsg.Text("Enter inches ")
ibox1 = fsg.InputText(key="feet")
ibox2 = fsg.InputText(key="inches")
b1 = fsg.Button("Convert")
b2 = fsg.Button("Exit")
output_label = fsg.Text("", key="output", text_color="Black")

layout = [[label1, ibox1], [label2, ibox2], [b1, b2, output_label]]

window = fsg.Window("Convertor", layout=layout, font=("Helvetica", 18))
while True:
    event, values = window.read()
    match event:
        case "Convert":
            feet = float(values["feet"])
            inches = float(values["inches"])
            meters = feet * 0.3048 + inches * 0.0254
            answer = f"{meters} m"
            window["output"].update(value=answer)

        case fsg.WIN_CLOSED:
            break

        case "Exit":
            break


window.close()
