import os

command_input = input()

while command_input != "End":
    parts = command_input.split("-")
    action = parts[0]
    file_name = parts[1]

    if action == "Create":
        with open(file_name, "w") as file:
            pass

    elif action == "Add":
        content = parts[2]
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif action == "Replace":
        old_string = parts[2]
        new_string = parts[3]

        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                file_contents = file.read()

            file_contents = file_contents.replace(old_string, new_string)

            with open(file_name, "w") as file:
                file.write(file_contents)

        else:
            print("An error occurred")

    elif action == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")

    command_input = input()