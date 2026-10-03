import os
from constants import path_to_dir

file_path = os.path.join(path_to_dir, 'files', 'my_first_file.txt')

try:
    os.remove(file_path)
    print("File deleted successfully!")
except FileNotFoundError:
    print("File already deleted!")