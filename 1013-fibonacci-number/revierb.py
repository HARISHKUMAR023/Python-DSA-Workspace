s = "(ed(et(oc))el)"
my=list(s)
for i in range(len(s)):
    if s[i] == ")" or s[i] == "(":
        my.pop(i)
        my.insert(i," ")
word=[]
w=""
for j in my:
    if j != " ":
        w+=j
    else:
      if w != '':
        word.append(w)
        w=""
f=""
ps=len(word)-1
while ps >= 0 :
     f+=word[ps]
     f+=' '
     ps-=1
print(f)

