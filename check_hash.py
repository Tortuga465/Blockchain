import hashlib
import os
import natsort as ns


def check_hashes(rel_path_dir):
    rel_path_dir=rel_path_dir+r"\text_files".strip()    #Записывает директорию с блоками
    file_list=os.listdir(rel_path_dir)[1:]              #Список файлов без .gitignore
    file_list=ns.natsorted(file_list)                      #Натуральная сортировка  массива
    hashes=[]
    for filename in file_list[1:]:
        if filename.endswith('.txt'):
            with open(os.path.join(rel_path_dir, filename)) as f:
                hash_line=f.readline().strip()
                hashes.append(hash_line)
    print(hashes)