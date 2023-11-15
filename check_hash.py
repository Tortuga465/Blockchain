import hashlib
import os
import natsort as ns


def check_hashes(rel_path_dir):
    rel_path_dir=rel_path_dir+r"\text_files".strip()    #Записывает директорию с блоками
    file_list=os.listdir(rel_path_dir)[1:]              #Список файлов без .gitignore
    file_list=ns.natsorted(file_list)                   #Натуральная сортировка  массива
    hashes_read=[]
    hashes_calc=[]
    for id, filename in enumerate(file_list[1:]):
        with open(os.path.join(rel_path_dir, filename)) as file_obj:            
            hash_line=file_obj.readline().strip()
            hashes_read.append(hash_line)

        with open(os.path.join(rel_path_dir,"chain{}".format(id+1)+".txt"), 'rb') as file_obj:
            file_contents=file_obj.read()
            md5_hash = hashlib.md5(file_contents).hexdigest()
            hashes_calc.append(md5_hash)
            #print("hash of a chain{} ".format(id)+"is {}".format(md5_hash))
    for id in range(len(hashes_read)):
        if(hashes_read[id]==hashes_calc[id]):
            print("Хэш блока {} валидно записан в блоке {}".format(id+1, id+2))
        else:
            print("Ошибка хэш блока {} в записи блока {}".format(id+1, id+2))
            break