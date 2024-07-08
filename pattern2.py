# # c=1
# # for i in range(1,6):
# #     for j in range(i,6):
# #       print(j , end=" ")
# #     for j in range(1, i):
# #         print(j, end=" ")
# #     print()
# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# def longestOnes():
#     left = 0
#     max_length = 0
#     zero_count = 0
#
#     for right in range(len(nums)):
#         if nums[right] == 0:
#             zero_count += 1
#
#         while zero_count > k:
#             if nums[left] == 0:
#                 zero_count -= 1
#             left += 1
#
#         max_length = max(max_length, right - left + 1)
#
#     return max_length
# print(longestOnes())
print(2 ^ 1)