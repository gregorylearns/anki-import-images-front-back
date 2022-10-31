import PySimpleGUI as sg 
import os


def generate_anki_deck_import(filelist):
    ankideck_generated = []
    i = 0
    while i < len(filelist):
        filea = f'<img src="{filelist[i]}"/>;<img src="{filelist[i+1]}"/>\n'
        ankideck_generated.append(filea)
        i += 2
        
    return(ankideck_generated)


###### GUI

sg.theme("LightBlue2")
layout = [
    [sg.Text('ANKI GENERATOR 0.1.0 - by grego')], 
    [sg.Text("(1) Select Folder (Folder must contain even number of images):")],
    [sg.In(size=(70,1), enable_events=True ,key='-FOLDER-'), sg.FolderBrowse()],
    [sg.Text("(2) Review the output pairings:")],
    [sg.Listbox(values=[], enable_events=True, horizontal_scroll=True, size=(80,10),key='-FILE LIST-')],
    [sg.Text("(3) Output File:")],
    [sg.In(size=(68,1), enable_events=True ,key='-OUTPUT-'), sg.FileSaveAs()],
    [sg.Text("(4) Generate Anki CSV for Import:"), sg.Button("Generate",key='-GENERATE-')],
    [sg.Text("(5) Paste your images to Anki's collection.media folder"), 
            sg.Button("Where is Anki Media Folder?", key='-OPEN-MEDIA-FOLDER-')]
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
        media_folder_text = """
            Refer to:                                                                          
            https://docs.ankiweb.net/files.html#file-locations
            
            Windows: "%APPDATA%\\Anki2" in your File Manager's Location Field
            Mac: ~/Library/Application Support/Anki2
            Linux: ~/.local/share/Anki2 /
            Linux(Flatpak): ~/.var/app/net.ankiweb.Anki/data/Anki2/Main/collection.media

            """
        sg.popup(media_folder_text, line_width=100, keep_on_top=True)
        # win_anki_dir = os.getenv('APPDATA')
        # path = os.path.realpath(win_anki_dir)
        # os.system(f"start {os.path.realpath(path)}")

    if event == '-FOLDER-':                         # Folder name was filled in, make a list of files in the folder
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)         # get list of files in folder
        except:
            file_list = []
        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
        fnames.sort()
        # window['-FILE LIST-'].update(fnames)
        window['-FILE LIST-'].update(generate_anki_deck_import(fnames))


        # Default Directory
        window['-OUTPUT-'].update(f"{folder}.csv")
   
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