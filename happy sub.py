from collections import defaultdict

nums = [1,0,1,0,1]
goal = 2
prefix_count = {}
prefix_count[0] = 1  # Base case to handle subarrays starting from index 0

current_sum = 0
result = 0

for num in nums:
    current_sum += num
    # Find how many times we have seen the prefix sum that would make the subarray sum equal to goal
    if (current_sum - goal) in prefix_count:
        result += prefix_count[current_sum - goal]
    # Update the prefix count
    if current_sum in prefix_count:
        prefix_count[current_sum] += 1
    else:
        prefix_count[current_sum] = 1

return result