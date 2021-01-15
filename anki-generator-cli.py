from sys import argv
from pathlib import PurePath
import os


# Usage: python anki-generator-cli.py /path/to/dir
# Output: /path/to/dir.txt



def get_filenames(folder):
    try:
        file_list = os.listdir(folder)         # get list of files in folder
    except:
        file_list = []
    fnames = [f for f in file_list if os.path.isfile(os.path.join(folder, f)) and 
        f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
    fnames.sort()
    return(fnames)


def generate_anki_deck_import(filelist):
    ankideck_generated = []
    i = 0
    while i < len(filelist):
        filea = f'<img src="{filelist[i]}"/>;<img src="{filelist[i+1]}"/>\n'
        ankideck_generated.append(filea)
        i += 2
        
    return ankideck_generated

def main():
    
    if len(argv) == 1:
        print("please input a directory"); return
    if len(argv) > 2:
        print("too many arguments"); return

    directory = argv[1]
    if directory[-1] != '/':
        directory += '/'

    filenames = get_filenames(directory)
    anki_file = generate_anki_deck_import(filenames)
    print(anki_file)

    directory_levels = directory.split('/')
    directory_levels = [x for x in directory_levels if len(x) > 0]
    save_file = f"{directory_levels.pop(-1)}.txt"
    print(save_file)
    print(directory_levels)
    save_location = f"/{'/'.join(directory_levels)}/"
    print(save_location)

    with open(save_location+save_file,'w') as outputfile:
        outputfile.writelines(anki_file)
    print("*"*50)
    print(f"Anki import file {save_file} generated successfully\n Please move images into anki media folder")
    return


if __name__ == "__main__":
    main()