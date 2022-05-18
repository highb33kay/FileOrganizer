import os
import shutil
import sys

try:
    # declare the path
    man = "C:\\Users\\HighB33Kay\\Desktop"
    
    # loop through the files in the folder
    for root,dir,files in os.walk(path):
        for file in files:
            ext = file.split(".")[1] 
            print(ext)
            if not os.path.exists(os.path.join(root,ext)):
                os.makedirs(os.path.join(root,ext))
            
            if os.path.exists(os.path.join(root,ext,file)):
                count = 1
                for newfile in os.listdir(os.path.join(root,ext,'')):
                    if name == "_".join(newfile.split(".")[0].split("_")[:-1]):
                        count += 1
                outfile = name+'_'+str(count)+'.'+ext
            else:
                output = file
            print('FIle:', os.path.join(root,file), '->', os.path.join(root,ext,outfile))
            func(os.path.join(root, file), os.path.join(root, ext, outfile))

            
except Exception:
    print(traceback.format_exc())