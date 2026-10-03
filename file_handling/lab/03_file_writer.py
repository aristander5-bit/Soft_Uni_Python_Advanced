import os
from constants import path_to_dir

file_path = os.path.join(path_to_dir, 'files', 'my_first_file.txt')

with open(file_path, 'w') as file:
    file.write("I just created my first file!")

print("The file is created successfully")