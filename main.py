import create_files
import check_hash
import os

# Инициализация
files_amount=int(input("Введите количество файлов\n"))
rel_path_dir=os.getcwd()
# Инициализация

#Функция создает блокчейн
create_files.crate_block_chain(files_amount, rel_path_dir)
#Функция проверяет блокчейн
#check_hash.check_hashes(rel_path_dir)