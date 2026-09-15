nums = tuple([float(x) for x in input().split()])

data = {}

for x in nums:
    if x not in data:
        data[x] = nums.count(x)

for key, value in data.items():
    print(f"{key:.1f} - {value} times")
