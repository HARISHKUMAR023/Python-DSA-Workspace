w="bbaacc"

def sortword(w):
    s = list(w)
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]> s[j]:
                t = s[i]
                s[i]=s[j]
                s[j]=t
            else:
                continue
    w=''.join(s)
    return w
if sortword("bbaacc") == "aabbc":
    print("Ture is working fine ")
else:
    print("________ Some thing working ________ ")