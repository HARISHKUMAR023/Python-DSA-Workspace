input_str = "pwwkew"
myset=set()
s=0
e=0
for i in range(len(input_str)):
    if input_str[e] in myset:
        myset.remove(input_str[e])
        # myset.remove(input_str[s])

        myset.add(input_str[e])

        s+=1
    else:
        myset.add(input_str[e])

    e+=1
print(myset)