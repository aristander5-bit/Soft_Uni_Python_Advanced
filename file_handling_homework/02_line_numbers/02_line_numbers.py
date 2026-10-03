from string import punctuation

with open("text.txt", "r") as input_file:
    lines = input_file.readlines()

output_lines = []

for index, line in enumerate(lines, start=1):
    line_str = line.strip("\n")

    letters_count = 0
    punctuation_count = 0

    for char in line_str:
        if char.isalpha():
            letters_count += 1
        elif char in punctuation:
            punctuation_count += 1

    formated_line = f"Line {index}: {line_str} ({letters_count} {punctuation_count})"
    output_lines.append(formated_line)

with open("output.txt", "w") as output_file:
    output_file.write("\n".join(output_lines))
