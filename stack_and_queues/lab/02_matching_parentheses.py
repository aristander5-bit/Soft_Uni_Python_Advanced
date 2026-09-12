expression = input()
parentheses_stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses_stack.append(i)
    elif expression[i] == ")":
        start_inx = parentheses_stack.pop()
        end_inx = i + 1
        print(expression[start_inx:end_inx])
