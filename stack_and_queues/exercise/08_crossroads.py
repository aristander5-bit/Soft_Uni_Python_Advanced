from collections import deque

green_duration = int(input())
free_window_duration = int(input())

cars = deque()
total_cars_passed = 0
has_crashed = False

while True:
    command = input()
    if command == "END":
        break
    if command == "green":
        current_green = green_duration

        while cars and current_green > 0:
            current_car = cars.popleft()
            car_length = len(current_car)

            if current_green >= car_length:
                current_green -= car_length
                total_cars_passed += 1
            else:
                remaining_car = car_length - current_green

                if free_window_duration >= remaining_car:
                    total_cars_passed += 1
                    current_green = 0
                else:
                    hit_index = current_green + free_window_duration
                    hit_character = current_car[hit_index]
                    print("A crash happened!")
                    print(f"{current_car} was hit at {hit_character}.")
                    has_crashed = True
                    break

        if has_crashed:
            break

    else:
        cars.append(command)

if not has_crashed:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")