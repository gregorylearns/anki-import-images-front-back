import PySimpleGUI as sg 
import os


def generate_anki_deck_import(filelist):
    ankideck_generated = []
    i = 0
    while i < len(filelist):
        filea = f'<img src="{filelist[i]}"/>;<img src="{filelist[i+1]}"/>\n'
        ankideck_generated.append(filea)
        i += 2
        
    return ankideck_generated


###### GUI

layout = [
    [sg.Text('ANKI GENERATOR 0.0.1 - by grego')], 
    [sg.Text("Folder") ,sg.In(size=(25,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Text("Input files")],
    [sg.Listbox(values=[], enable_events=True, size=(40,10),key='-FILE LIST-')],
    [sg.Text("Output File:")],
    [sg.In(size=(25,1), enable_events=True ,key='-OUTPUT-'), sg.FileSaveAs()],
    [sg.Button("Generate",key='-GENERATE-'), sg.Button("Open Anki Media Folder", key='-OPEN-MEDIA-FOLDER-')]
]



# --------------------------------- Create Window ---------------------------------
window = sg.Window('Anki Table Generator 0.0.1', layout, resizable=True)


# ----- Run the Event Loop -----
# --------------------------------- Event Loop ---------------------------------
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-OPEN-MEDIA-FOLDER-':
        win_anki_dir = os.getenv('APPDATA')
        path = os.path.realpath(win_anki_dir)
        os.system(f"start {os.path.realpath(path)}")

    if event == '-FOLDER-':                         # Folder name was filled in, make a list of files in the folder
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)         # get list of files in folder
        except:
            file_list = []
        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
        fnames.sort()
        window['-FILE LIST-'].update(fnames)
   
    if event == '-OUTPUT-':
        save_as = values['-OUTPUT-']


    elif event == '-GENERATE-':
        try:
            generated_anki = generate_anki_deck_import(fnames)
            with open(save_as,'w') as outputfile:
                outputfile.writelines(generated_anki)
                sg.popup(f"Anki import file {save_as} generated successfully\n Please move images into anki media folder",
                    keep_on_top=True)
        except NameError:
            sg.PopupError("Please Select a Folder/ Select output file")


    
# --------------------------------- Close & Exit ---------------------------------
window.close()