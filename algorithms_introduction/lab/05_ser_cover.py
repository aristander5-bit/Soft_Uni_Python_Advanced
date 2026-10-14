# def solve_set_cover(universe, sets):
#     selected_sets = []
#
#     while universe:
#         best_set = max(sets, key=lambda s: len(universe.intersection(s)))
#         selected_sets.append(best_set)
#         universe -= best_set
#         sets.remove(best_set)
#
#     return selected_sets
#
# universe_line = input()
# if ":" in universe_line:
#     universe = set(int(x) for x in universe_line.split(": ")[1].split(", "))
# else:
#     universe = set(int(x) for x in universe_line.split(", "))
#
# try:
#     n = int(input())
# except ValueError:
#     n = 0
#
# sets = []
#
# while True:
#     try:
#         line = input()
#         if not line:
#             break
#
#         cleaned_line = line.replace("{", "").replace("}", "")
#         current_set = set(int(x) for x in cleaned_line.split(", "))
#         sets.append(current_set)
#     except EOFError:
#         break
#
# result = solve_set_cover(universe, sets)
#
# print(f"Sets to take ({len(result)}):")
# for s in result:
#     print("{ " + ", ".join(str(x) for x in sorted(s)) + " }")

# def solve_set_cover(universe, sets):
#     selected_sets = []
#
#     while universe:
#         best_set = max(sets, key=lambda s: len(universe.intersection(s)))
#
#         selected_sets.append(best_set)
#         universe -= best_set
#         sets.remove(best_set)
#
#     result = f"Sets to take ({len(selected_sets)}):\n"
#     for s in selected_sets:
#         elements = ", ".join(str(x) for x in sorted(s))
#         result += f"{{ {elements} }}\n"
#
#     return result.strip()
#
# universe = set(int(x) for x in input().split(", "))
#
# try:
#     n = int(input())
# except ValueError:
#     pass
#
# sets = []
# while True:
#     try:
#         line = input()
#         if not line:
#             break
#
#         cleaned = line.replace("{", "").replace("}", "")
#         current_set = set(int(x) for x in cleaned.split(", "))
#         sets.append(current_set)
#     except EOFError:
#         break
#
# print(solve_set_cover(universe, sets))

def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:
        best_set = max(remaining_sets, key=lambda s: len(universe_set.intersection(s)))
        if not universe_set.intersection(best_set):
            break

        chosen_sets.append(best_set)
        universe_set -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_set:
        return None
    return chosen_sets

universe = list(map(int, input().split(", ")))
n = int(input())
sets = []

for _ in range(n):
    line = input()
    cleaned = line.replace("{", "").replace("}", "").strip()
    if "," in cleaned:
        set_elements = [int(x) for x in cleaned.split(",")]
    else:
        set_elements = [int(x) for x in cleaned.split()]
    sets.append(set_elements)

result = set_cover(universe, sets)

if result is None:
    print("No solution exist")
else:
    print(f"Sets to take ({len(result)}):")
    for s in result:
        sorted_s = sorted(s)
        elements_str = ", ".join(str(x) for x in sorted_s)
        print(f"{{ {elements_str} }}")


