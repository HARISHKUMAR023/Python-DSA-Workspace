def twosum(nums, target):
    my = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in my:
            # print(my)
            return my[complement], i
        my[nums[i]] = i
    return None


nums = [3, 3]
target = 6
result = twosum(nums, target)

print(result)
