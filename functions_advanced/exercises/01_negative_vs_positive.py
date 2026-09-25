def nums_sums(*args):
    n_sum =0
    p_sum = 0
    for number in args:
        if number > 0:
            p_sum += number
        else:
            n_sum += number
    return n_sum, p_sum

nums = map(int, input().split())
negative_nums, positive_nums = nums_sums(*nums)

print(negative_nums)
print(positive_nums)
if abs(negative_nums) > abs(positive_nums):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
