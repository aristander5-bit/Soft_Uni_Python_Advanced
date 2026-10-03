import os
from file_handling.lab.constants import path_to_dir

file_path = os.path.join(path_to_dir, 'files', 'numbers.txt')

total_sum = 0

with open(file_path, 'r') as file:
    for line in file:
        total_sum += int(line.strip())

print(total_sum)