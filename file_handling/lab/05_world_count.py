import os
import re
from constants import path_to_dir

words_path = os.path.join(path_to_dir, 'files', 'words.txt')
input_path = os.path.join(path_to_dir, 'files', 'input.txt')
output_path = os.path.join(path_to_dir, 'files', 'output.txt')

with open(words_path, 'r') as words_file:
    searched_words = words_file.read().lower().split()

with open(input_path, 'r') as input_file:
    text = input_file.read().lower()

word_counts = {}

for word in searched_words:
    matches = re.findall(rf"\b{word}\b", text)
    word_counts[word] = len(matches)

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

with open(output_path, 'w') as output_file:
    for word, count in sorted_words:
        result_line = f"{word} - {count}\n"
        output_file.write(result_line)
        print(f"{word} - {count}")