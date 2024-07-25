w="harish"
def reverseword(w):
        ans=""
        for i in range(len(w)-1, -1,-1 ):
             ans+=w[i]
        return ans
print(reverseword(w))