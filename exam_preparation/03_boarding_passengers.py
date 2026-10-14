def boarding_passengers(capacity, *passenger_groups):
    boarded = {}
    passengers_waiting = False

    for passengers, program in passenger_groups:
        if passengers <= capacity:
            boarded[program] = boarded.get(program, 0) + passengers
            capacity -= passengers
        else:
            passengers_waiting = True
            if capacity <= 0:
                break

    sorted_passengers = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))

    result = ["Boarding details by benefit plan:"]
    for program, passengers in sorted_passengers:
        result.append(f"## {program}: {passengers} guests")
    if not passengers_waiting:
        result.append("All passengers are successfully boarded!")
    elif capacity <= 0:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")
    return "\n".join(result)


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))
