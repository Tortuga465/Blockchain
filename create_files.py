import lorem
import os.path
import hashlib

folder_dir = "\\text_files\\" # Нахождение в папке с создаваемыми файлами

#Функция создания файлов
def create_file(files_amount: int, rel_path_dir: str): #Функция принимает два параметра: files_amount (количество файлов) и rel_path_dir (относительный путь к директории).
    
    names_files = list() #Записывает имена файлов

    for i in range(1, files_amount+1): #Выполняется цикл от 1 до files_amount+1.
        templ_name = f"chain{i}.txt" #Шаблон имени файла

        #Создание файла/ов
        f=open(rel_path_dir+folder_dir+templ_name,"w") 
        f.close()

        #Добавление в лист имён
        names_files.append(templ_name)

    return names_files #Возрат имён файлов в main
        

    

def create_block_chain(files_amount: int, rel_path_dir: str):              #name_list: list    
    
    for i in range(1, files_amount+1): #Выполняется цикл от 1 до files_amount+1.
        rel_path_file=os.path.join(rel_path_dir,"text_files\chain{}".format(i)+".txt") #Создается относительный путь к файлу, используя функцию os.path.join и значение i.
        f=open(rel_path_file,"w")
        

        md5_hash=""
        if(i>1):
            with open(os.path.join(rel_path_dir,"text_files\chain{}".format(i-1)+".txt"), 'rb') as file_obj:
                file_contents = file_obj.read()
                md5_hash = hashlib.md5(file_contents).hexdigest()
                f.write(md5_hash)
                f.write("\n")
        f.close
        f=open(rel_path_file,"rb")
        file_contents_f = f.read()
        print(file_contents_f)
        while(hashlib.md5(file_contents_f).hexdigest()[:2]!="00"):
            f.close
            f=open(rel_path_file,"a")
            f.write(lorem.sentence())
            f.close
            f=open(rel_path_file,"rb")
            file_contents_f = f.read()
        f.close