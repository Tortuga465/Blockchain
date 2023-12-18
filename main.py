from create_files import create_block_chain, create_file
from check_hash import check_hashes
import os

def main():

    action="" # Выбор действия пользователя: создание, проверка, выход
    files_names = [] #Список имён файлов
    rel_path_dir = os.getcwd() #Путь

    while ("check" != action and "create"!=action and "exit"!=action):
        action=input("enter action: \ncreate - создание блокчейна\ncheck - проверка блокчейна на валдиность\nexit - выход из программы\n")
    
    if(action=="create"):
        files_amount = int(input("Введите количество файлов\n")) #Количество файлов
        #Функция создает файлы
        files_names = create_file(files_amount, rel_path_dir) 
        print(len(files_names), files_names)  #Проверка функции
        
        #Функция создаёт цепочки
        create_block_chain(files_names, rel_path_dir)
    
    if(action=="check"):
        #Функция проверяет блокчейн
        check_hashes(rel_path_dir)

    if(action=="exit"):
        exit
        
if __name__ == '__main__':
    main()