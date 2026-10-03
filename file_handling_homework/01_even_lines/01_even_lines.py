REPLACEMENT = {"-", ",", ".", "!", "?"}

with open("text.txt", "r") as file:
    lines = file.readlines()

for index in range(0, len(lines), 2):
    line = lines[index]

    for char in REPLACEMENT:
        line = line.replace(char, "@")

    words = line.split()
    reversed_line = " ".join(words[::-1])

    print(reversed_line)