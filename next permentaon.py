nums = [1,2,3]
per = []
for i in range(len(nums)):

    for j in range(i + 1, len(nums)):
        ans = [nums[i]]
        ans.append(nums[j])
        per.append((ans))
print(per)