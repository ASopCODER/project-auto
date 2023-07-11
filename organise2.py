import os
import shutil

from_dir="C:/Users/admin/Downloads"
to_dir="c:/Users/admin/Documents"
list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(name)
    print(extention)

    if(extention==""):
        continue
    if extention in[".gif",".png",".jpg",".jpeg",]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image_files"
        path3=to_dir+"/"+"image_files"+"/"+file_name

        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            