from pathlib import Path
import shutil
import sys


def sortDirectory(directory, func=shutil.copy):
    # declare the directory
    root = Path(directory)
    # if it is not the root directory return false
    if not root.is_dir():
        return 1
    # for each entry in root
    for entry in root.iterdir():
        # if not file exit the program
        if not entry.is_file():
            continue
        name = entry.stem
        ext = entry.suffix[1:]
        print(ext)
        # make output folder out and ext
        Path(Path("out") / Path(ext)).mkdir(parents=True, exist_ok=True)
        
        # if Path(Path("out") / ext / entry.name).exists():
        #     count = 1
        #     for newfile in Path(Path("out/ext") / entry.name).iterdir():
        #         if name == "_".join(newfile.split('.')[0].split('_')[:-1]):
        #             count += 1
        #     outfile = name+'_'+str(count)+'.'+ext
        # else:
        #     output = entry
        # print('File:', Path(root / ext / entry.name), '->', Path(Path("out") / ext / entry.name))
        func(Path(root),Path("out/ext/entry.name"))
        print('moving'+ext)
    return 0

def main():
    
    
    functionDict = {
        'm': shutil.move,
        'c': shutil.copy,
    }
    flag = shutil.copy
    if len(sys.argv) == 3:
        if sys.argv[2].lower()[0] in functionDict:
            flag = functionDict[sys.argv[2].lower()[0]]
        else:
            print("Unsupported 3rd argument. Use 'm'ove or 'c'opy")
            return 1

    elif len(sys.argv) == 1 or len(sys.argv) > 3:
        print(
            "Wrong amount of arguments. Only 2 arguments supported: [path function]")
        return 1

    return sortDirectory(sys.argv[1], flag)


if __name__ == '__main__':
    main()