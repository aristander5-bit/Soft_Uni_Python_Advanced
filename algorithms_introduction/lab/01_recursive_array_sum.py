def calculate_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]

    return numbers[idx] + calculate_sum(numbers, idx + 1)

nums = [int(x) for x in input().split()]

print(calculate_sum(nums, idx=0))
