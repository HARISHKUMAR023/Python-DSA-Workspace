nums = [-2,0,-1]
pro = 0
for i in range(len(nums)-1):
    ans = nums[i]
    ans = nums[i] * nums[i+1]
    pro=max(ans,pro)

print(pro)