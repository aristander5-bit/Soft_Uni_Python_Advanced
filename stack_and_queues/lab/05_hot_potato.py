from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    kids.rotate(1 - n)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids[0]}")