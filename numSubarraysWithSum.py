nums = [1,0,1,0,1]
goal = 2
ans = 0
for i in range(0, len(nums)):
    c = nums[i]
    for j in range(i + 1, len(nums)):
        if c == goal:
            ans += 1
            c=0
        c += nums[j]
print(c)