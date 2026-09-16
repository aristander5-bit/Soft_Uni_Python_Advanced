from collections import deque

colors_string = deque(input().split())
main_colors = {"red", "yellow", "blue"}
second_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}
collected_colors = []

while colors_string:
    first_str = colors_string.popleft()
    last_str = colors_string.pop() if colors_string else ""

    for color in (first_str + last_str, last_str + first_str):
        if color in main_colors or color in second_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_str) > 1:
            colors_string.insert(len(colors_string) // 2, first_str[:-1])
        if len(last_str) > 1:
            colors_string.insert(len(colors_string) // 2, last_str[:-1])

valid_colors = []
for color in collected_colors:
    if color in main_colors:
        valid_colors.append(color)
    elif color in second_colors:
        for c in second_colors[color]:
            if c not in collected_colors:
                break
        else:
            valid_colors.append(color)

print(valid_colors)
