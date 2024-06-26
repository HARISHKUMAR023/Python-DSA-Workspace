a = "     hii   hello   welcome   "
ans=""
wordposion=[]
p1=0
p2=0
c=0
for  i in a:
    if i != " ":
        
        wordposion.append(c)
    c+=1 
# print(wordposion)
p=[]
p.append(wordposion[0])
for j in range(len(wordposion)-1):
    if wordposion[j+1] - wordposion[j]   != 1:
        p.append(wordposion[j])
        p.append(wordposion[j+1])


# print(p)
ts=""
tsp=0
for s in a[p[-1]:-1]:
    if s != " ":
       ts+=s
    tsp+=1
# print(ts,tsp)
      
 
ans1=""
p1=0
p2=1
ans1=""
for k in range(len(p)):
    if p2 == len(p):
        break
    ans1+= a[p[p1] : p[p2]+1]
    ans1+=" "
  
    p1+=2
    p2+=2
ans1+=ts
   

print(ans1)
print(p[0])

t=p[-1]-p[-1]
print(tsp-len(ts)+1)

ps1=1
ps2=2
middle =0
for k in range(len(p)):
    if ps2 == len(p)+1:
        break
    gt= p[ps2] - p[ps1]
   
    middle+=gt
    ps1+=2
    ps2+=2
tsr=0
for hs in range(2,len(p)-1):
    tsr+=1

if middle == 2:
    print (1)
else:
  print(middle-2 - tsr)
