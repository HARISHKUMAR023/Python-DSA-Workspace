s = "words and 987"
v=s.lstrip()
ans=""
for i in v:
    if 'a' <= v[0] <= 'z' or 'A' <= v[0] <= 'Z':
        print(0)
        break
    if v[0] != "-":
        if i == '+' or i == '-' or i ==  '.' or i == '_' or 'a' <= i <= 'z' or 'A' <= i <= 'Z':
             # print(0)
             # ans=0
             break
        else:
            ans+=i
    else:
        ans+=i
print(ans)
# else:
#    print(int(v))