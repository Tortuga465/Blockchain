import create_files
import check_hash
import os

def main():

    file_names = [] #Список имён файлов

    files_amount = int(input("Введите количество файлов\n")) #количество файлов
    rel_path_dir = os.getcwd() #количество файлов
    
    #Функция создает блокчейн
    #create_files.crate_block_chain(files_amount, rel_path_dir)
    #Функция проверяет блокчейн
    #check_hash.check_hashes(rel_path_dir)



if __name__ == '__main__':
    main()