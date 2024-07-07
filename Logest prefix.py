strs = []
s=0
e=1
ans=""
if len(strs) == 0:
    return ans
minlen=len(strs[0])
for i in strs:
    if len(i) < minlen:

        minlen = len(i)


for i in range(minlen):
    for j in range(len(strs)):
        if strs[0][s:e] not in strs[j][s:e] :
             break
    else:
        ans+=strs[0][s:e]
        s += 1
        e += 1


print(ans)

# print(p)
# f=p[s:e]
# ans=""
# for j in strs:
#     if f != j[s:e]:
#         break
#     else:
#         e+=1


# for j in range(minlen):
#     sub=""
#     t=k[s:e]
#     for k in strs:
#         if t in k[]
#     sub+=k[s:e]
