import os

files = {}
directory = "./"

def get_files(folder, level=1):
    if level < 0:
        return

    for element in os.listdir(folder):
        file_path = os.path.join(folder, element)

        if os.path.isfile(file_path):
            if element in ("report.txt", "04_directory_traversal.py"):
                continue

            _, extension = os.path.splitext(element)
            if extension:
                if extension not in files:
                    files[extension] = []
                files[extension].append(element)

        elif os.path.isdir(file_path):
            get_files(file_path, level - 1)

get_files(directory, level=1)

with open(os.path.join(directory, "report.txt"), "w") as output:
    for extension, filenames in sorted(files.items()):
        output.write(f"{extension}\n")
        for filename in sorted(filenames):
            output.write(f"- - - {filename}\n")
