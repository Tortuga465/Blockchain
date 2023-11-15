import hashlib
import os

def check_hashes(rel_path_dir):
    rel_path_dir=rel_path_dir+r"\text_files".strip()
    for filename in os.listdir(rel_path_dir)[2:]:
        if filename.endswith('.txt'):
            with open(os.path.join(rel_path_dir, filename)) as f:
                print(f.readline().strip())
