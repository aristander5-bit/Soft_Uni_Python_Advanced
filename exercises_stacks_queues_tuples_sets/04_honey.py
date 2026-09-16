from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 0
}


while bees and nectar:
    current_nectar = nectar.pop()

    if current_nectar >= bees[0]:
        current_bee = bees.popleft()
        current_symbol = symbols.popleft()
        honey += abs(operators[current_symbol](current_bee, current_nectar))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
elif nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
