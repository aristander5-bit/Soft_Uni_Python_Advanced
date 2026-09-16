from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque([int(x) for x in input().split(", ")])

milkshakes = 0

while milkshakes < 5 and chocolates and milk_cups:
    chocolate = chocolates[-1]
    milk = milk_cups[0]

    if chocolate <= 0 or milk <= 0:
        if chocolate <= 0:
            chocolates.pop()
        if milk <= 0:
            milk_cups.popleft()
        continue

    if chocolate == milk:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milk_cups)) if milk_cups else 'empty'}")
