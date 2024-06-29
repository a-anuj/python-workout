import FreeSimpleGUI as fsg
import make_archive_function

label1 = fsg.Text("Choose files to compress ")
input_box1 = fsg.InputText(key="filename")
button1 = fsg.FilesBrowse(key="File")
label2 = fsg.Text("Choose the destination folder ")
input_box2 = fsg.InputText(key="")
button2 = fsg.FolderBrowse(key="Folder")
compress_button = fsg.Button("Compress")
output_label = fsg.Text(key="output",text_color="green")
layout = [[label1, input_box1, button1], [label2, input_box2, button2],
          [compress_button, output_label]]
window = fsg.Window("File compressor", layout=layout)


while True:
    event, values = window.read()
    print("Event : ", event)
    print("Values : ", values)
    match event:
        case "Compress":
            filepath = values["File"].split(";")
            dirtry = values["Folder"]
            make_archive_function.make_archive(filepath, dirtry)
            window["output"].update(value="Compressed Successfully :) ")
        case fsg.WIN_CLOSED:
            break


window.close()
