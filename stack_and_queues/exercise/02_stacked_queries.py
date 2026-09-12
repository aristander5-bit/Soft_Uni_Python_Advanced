# n = int(input())
# stack = []
#
# for _ in range(n):
#     query = input().split()
#
#     if query[0] == "1":
#         stack.append(int(query[1]))
#     elif stack:
#         if query[0] == "2":
#             stack.pop()
#         elif query[0] == "3":
#             print(max(stack))
#         elif query[0] == "4":
#             print(min(stack))
#
# print(", ".join([str(x) for x in reversed(stack)]))

n = int(input())
stack = []

functions = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None,

}

for _ in range(n):
    query = input().split()
    functions[query[0]](*query[1:])

print(*reversed(stack), sep=", ")


