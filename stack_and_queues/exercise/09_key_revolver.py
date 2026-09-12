from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(x) for x in input().split()]

locks = deque([int(x) for x in input().split()])

intelligence_value = int(input())

shot_bullets = 0
current_barrel = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]

    shot_bullets += 1
    current_barrel += 1

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if current_barrel == barrel_size and bullets:
        print("Reloading!")
        current_barrel = 0

if not locks:
    money_earned = intelligence_value - (shot_bullets * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")