def bubble_sort(nums):
    is_sorted = False
    sorted_elements = 0

    while not is_sorted:
        is_sorted = True
        for j in range(1, len(nums) - sorted_elements):
            i = j - 1
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                is_sorted = False
        sorted_elements += 1

numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)