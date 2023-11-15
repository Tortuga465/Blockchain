import hashlib
import os
import natsort as ns


def check_hashes(rel_path_dir):
    rel_path_dir=rel_path_dir+r"\text_files".strip()
    file_list=os.listdir(rel_path_dir)[1:]          #removes .gitignore
    print(ns.natsorted(file_list))
    for filename in file_list[2:]:
        if filename.endswith('.txt'):
            with open(os.path.join(rel_path_dir, filename)) as f:
                print(f.readline().strip())
