import lorem
import os.path
import hashlib


def crate_block_chain(files_amount, rel_path_dir):
                             
# Относительный путь. На Линукс не будет работать, т.к. формат пути другой
      # Путь до файла
    
    for i in range(1, files_amount+1):
        rel_path_file=os.path.join(rel_path_dir,"text_files\chain{}".format(i)+".txt")
        f=open(rel_path_file,"w")
        md5_hash=""
        if(i>1):
            with open(os.path.join(rel_path_dir,"text_files\chain{}".format(i-1)+".txt"), 'rb') as file_obj:
                file_contents = file_obj.read()
                md5_hash = hashlib.md5(file_contents).hexdigest()
                f.write(md5_hash)
                f.write("\n")
        f.write(lorem.sentence())
        f.close