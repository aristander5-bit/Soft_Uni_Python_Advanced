from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_weight = 0

while packages and couriers:
    package = packages[-1]
    courier = couriers.popleft()

    if courier >= package:
        total_weight += package
        packages.pop()
        courier -= package * 2
        if courier > 0:
            couriers.append(courier)
    else:
        packages[-1] -= courier
        total_weight += courier

print(f"Total weight: {total_weight} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages))}")
elif not packages and couriers:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")
