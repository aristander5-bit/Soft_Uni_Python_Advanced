from collections import deque

expression = input().split()
numbers = deque()

operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}

for character in expression:
    if character not in "+-*/":
        numbers.append(int(character))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            numbers.appendleft(operators[character](first_num, second_num))

print(numbers[0])
