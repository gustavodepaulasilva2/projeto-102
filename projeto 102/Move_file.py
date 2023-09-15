import os
import shutil

from_dir = "C:/Users/Gustavo/Downloads/projeto 102"
to_dir  = "C:/Users/Gustavo/Desktop/Arquivos_Documentos/"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == "":
        continue
    if extension in [".png", ".jpeg", ".jpe",".gif", ".jfif"]:
        path1 = from_dir + "/" + file_name
        path2 = to_dir
        path3 = to_dir + "/" + file_name

        if os.path.exists(path2):
            print("movendo os arquivos...")
            shutil.move(path1, path3)
        else:
            print("criando pasta nova..." )
            os.makedirs(path2)
            print("movendo os arquivos...")
            shutil.move(path1, path3)
