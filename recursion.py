n=5
# for  i in range(n):
# for k in range(1,n):
#     for i in range(1,n):
#        print("_" * n-1 ,end="")
#     print()

for j in range(1,n):
    print("_" * (n-j) ,end= "")
    print("*" * j , end = "")
    print("_" *j , end="")
    print()