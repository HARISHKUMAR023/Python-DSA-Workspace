# arr = [1,2,3,4]
# k = 2
def findKthPositive():
    arr = [1, 2, 3, 4]
    k = 2
    ans = []
    for i in range(1, arr[-1]):
        if i not in arr:
            ans.append(i)
    print(ans)
    # return ans[k-1]
print(findKthPositive())