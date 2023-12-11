from create_files import create_block_chain, create_file
from check_hash import check_hashes
import os

def main():

    files_names = [] #Список имён файлов

    files_amount = int(input("Введите количество файлов\n")) #Количество файлов
    rel_path_dir = os.getcwd() #Путь
    
    #Функция создает файлы
    files_names = create_file(files_amount, rel_path_dir) 
    #print(len(files_names), files_names)  #Проверка функции
    
    #Функция создаёт цепочки
    create_block_chain(files_names, rel_path_dir)


    #Функция проверяет блокчейн
    #check_hash.check_hashes(rel_path_dir)



if __name__ == '__main__':
    main()