import os

while True:
    line = input()
    if line == 'End':
        break

    command, filename, *args = line.split("-")

    if command == 'Create':
        open(filename, "w").close()
    elif command == "Add":
        with open(filename, "a") as file:
            file.write(f"{args[0]}\n")

    elif command == "Replace":
        try:
            with open(filename, "r+") as file:
                old_string, new_string = args
                content = file.read()
                file.seek(0)
                file.truncate(0)
                file.write(content.replace(old_string, new_string))
        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        # if os.path.exists(filename):
        #     os.remove(filename)
        # else:
        #     print("An error occurred")
        try:
            os.remove(filename)
        except FileNotFoundError:
            print("An error occurred")
