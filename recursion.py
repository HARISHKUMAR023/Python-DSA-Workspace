s=0
n=6
r=n-1

for i in range(s,n):
    for j in range(n):
        if i == s:
            print(j , end=" ")
        elif j == 0:
            print(i,end=" ")
        elif j == n-1:
            print(i, end=" ")
        elif i == n-1:
            print(j,end=" ")
        else:
            print("*", end=" ")
    print()
# for i in range(n):
#     # print(i)
#     for j in range(n):
#         if i == j:
#             print("*", end=" ")
#         elif j == r:
#             print("*" , end=" ")
#         else:
#             print(" ",end=" ")
#     r-=1
#     print()