# numbers = list(map(int, input().split()))
# target = int(input())
#
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(f"{numbers[i]} + {numbers[j]} = {target}")
#             for i in range(len(numbers)):
#                 if numbers[i] == '':
#                     continue
#                 for j in range(i + 1, len(numbers)):
#                     if numbers[j] == '':
#                         continue
#                     if numbers[i] + numbers[j] == target:
#                         print(f"{numbers[i]} + {numbers[j]} = {target}")
#                         numbers[i] = ''
#                         numbers[j] = ''
#                         break
#
# numbers = list(map(int, input().split()))
# target = int(input())
#
# targets = set()
# values_map = {}
#
# for value in numbers:
#     resulting_number = target - value
#     targets.add(resulting_number)
#     values_map[resulting_number] = value
#
# for value in numbers:
#     if value not in targets:
#         targets.remove(value)
#         pair = values_map[value]
#         del values_map[value]
#         print(f'{pair} + {value} = {target}')
#     else:
#         resulting_number = target - value
#         targets.add(resulting_number)
#         values_map[resulting_number] = value

import time

numbers = list(map(int, input().split()))
target = int(input())

start = time.time()
targets = set()
values_map = {}

for value in numbers:
    if value in targets:
        targets.remove(value)
        pair = values_map[value]
        del values_map[value]
        print(f'{pair} + {value} = {target}')
    else:
        resulting_number = target - value
        targets.add(resulting_number)
        values_map[resulting_number] = value
end = time.time()
print(f"Time range: {end - start}")
