from collections import deque

robots_data = input().split(";")
robots = []
for robot in robots_data:
    robot_name, process_time = robot.split("-")
    robots.append({"name": robot_name, "process_time": int(process_time), "busy_until": 0})

hours, minutes, seconds = [int(x) for x in input().split(":")]
start_time_seconds = hours * 3600 + minutes * 60 + seconds

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    current_product = products.popleft()
    start_time_seconds += 1

    robot_assigned = False

    for r in robots:
        if r["busy_until"] <= start_time_seconds:
            r["busy_until"] = start_time_seconds + r["process_time"]

            h = (start_time_seconds // 3600) % 24
            m = (start_time_seconds % 3600) // 60
            s = start_time_seconds % 60


            print(f"{r['name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")
            robot_assigned = True
            break
    if not robot_assigned:
        products.append(current_product)