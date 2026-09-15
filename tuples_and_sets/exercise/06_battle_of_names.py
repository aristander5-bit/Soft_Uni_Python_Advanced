even_set = set()
odd_set = set()

for r in range(1, int(input()) + 1):
    current_number = sum(ord(ch) for ch in input()) // r
    if current_number % 2 == 0:
        even_set.add(current_number)
    else:
        odd_set.add(current_number)

if sum(even_set) == sum(odd_set):
    print(*odd_set.union(even_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')