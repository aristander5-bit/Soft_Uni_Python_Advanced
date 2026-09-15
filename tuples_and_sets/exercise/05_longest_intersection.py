def create_set_from_range(range_str):
    start, end = range_str.split(",")
    return set(range(int(start), int(end) + 1))

longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    # first_start, first_end = [int(x) for x in first_range.split(",")]
    # second_start, second_end = [int(x) for x in second_range.split(",")]

    # first_set = set(range(first_start, first_end + 1))
    # second_set = set(range(second_start, second_end + 1))

    first_set = create_set_from_range(first_range)
    second_set = create_set_from_range(second_range)

    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")

