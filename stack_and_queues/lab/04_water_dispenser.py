from collections import deque

litters = int(input())
people = deque()

line = input()

while line != "Start":
    people.append(line)
    line = input()

while line != "End":
    if line.isdigit():
        person = people.popleft()
        litters_needed = int(line)
        if litters >= litters_needed:
            litters -= litters_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    elif line.startswith("refill"):
        litters += int(line.split()[1])

    line = input()

print(f"{litters} liters left")