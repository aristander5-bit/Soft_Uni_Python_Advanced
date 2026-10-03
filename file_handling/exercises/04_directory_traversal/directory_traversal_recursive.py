import os

files = {}
directory = "../"

def get_files(folder, level=float("inf")):
    if level < 0:
        return

    for element in os.listdir(folder):
        f = os.path.join(folder, element)

        if os.path.isfile(f):
            _, ext = os.path.splitext(element)
            if ext:
                if ext not in files:
                    files[ext] = []
                files[ext].append(element)

        elif os.path.isdir(f):
            get_files(f, level - 1)

get_files(directory)


with open(os.path.join(directory, "report.txt"), "w") as output:
    for ext, filenames in sorted(files.items()):
        output.write(f"{ext}\n")
        for file_name in sorted(filenames):
            output.write(f"- - - {file_name}\n")