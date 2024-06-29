import FreeSimpleGUI as fsg
import backend

fsg.theme("DarkBlue")
label1 = fsg.Text("Choose file ")
label2 = fsg.Text("Choose folder ")
ibox1 = fsg.InputText()
ibox2 = fsg.InputText()
b1 = fsg.FilesBrowse("Choose", key="file")
b2 = fsg.FolderBrowse("Choose", key="folder")
b3 = fsg.Button("Extract")
output_text = fsg.Text("", key="output", text_color="Green")

layout = [[label1, ibox1, b1], [label2, ibox2, b2], [b3, output_text]]

window = fsg.Window("Files Extractor", layout=layout, font=("Tahoma", 18))
while True:
    event, values = window.read()
    match event:
        case "Extract":
            filepath = values["file"]
            dstn_dir = values["folder"]
            backend.unzip_file(filepath, dstn_dir)
            window["output"].update(value="Extracted Successfully !")
        case fsg.WIN_CLOSED:
            break

window.close()
