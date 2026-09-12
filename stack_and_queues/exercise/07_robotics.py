from collections import deque
from datetime import datetime, timedelta

robots_data = input().split(";")
robots = []

for robot in robots_data:
    name, time = robot.split("-")
    process_time = int(time)
    robots.append({
        "name": name,
        "process_time": process_time,
        "free_at": 0
    })

start_time = input()
current_time = datetime.strptime(start_time, "%H:%M:%S")

products = deque()

while True:
    command = input()
    if command == "End":
        break
    products.append(command)

total_seconds = 0

while products:
    total_seconds += 1
    current_product = products.popleft()
    current_time += timedelta(seconds=1)

    robot_assigned = False

    for robot in robots:
        if total_seconds >= robot["free_at"]:
            robot["free_at"] = total_seconds + robot["process_time"]
            robot_assigned = True
            time_formatted = current_time.strftime("%H:%M:%S")
            print(f"{robot['name']} - {current_product} [{time_formatted}]")
            break

    if not robot_assigned:
        products.append(current_product)
