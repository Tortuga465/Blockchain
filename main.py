import create_files
import check_hash
import os

# INITITALISE DIR
#files_amount=int(input("enter number of files\n"))
rel_path_dir=os.getcwd()

# INITIALISE DIR


#create_files.crate_block_chain(files_amount, rel_path_dir)
check_hash.check_hashes(rel_path_dir)