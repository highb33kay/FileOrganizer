# file organizer that sorts files into folders based on their extension
from pathlib import Path
from shutil import copy
from sys import argv


def sortDirectory(directory, func=copy):
    # declare the directory
    root = Path(directory)
    # if it is not the root directory return false
    if not root.is_dir():
        return 1
    # for each entry in root
    for entry in root.iterdir():
        # if not file exit the program
        if entry.is_file():
            name = entry.stem
            ext = entry.suffix[1:]
            print(ext)
            # make output folder out and ext
            Path(Path("out") / Path(ext)).mkdir(parents=True, exist_ok=True)

            if Path(Path("out") / ext / entry.name).exists():
                count = 1
                for newfile in Path(Path("out/ext") / entry.name).iterdir():
                    if name == "_".join(newfile.split('.')[0].split('_')[:-1]):
                        count += 1
                outfile = name+'_'+str(count)+'.'+ext
            else:
                output = entry
            print('File:', Path(root / ext / entry.name),
                  '->', Path(Path("out") / ext / entry.name))
            func(Path(root), Path("out/ext/entry.name"))
            print('moving'+ext)
    return 0
