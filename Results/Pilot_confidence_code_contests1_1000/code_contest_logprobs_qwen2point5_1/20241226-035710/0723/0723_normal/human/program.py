l = map(int,raw_input().split())
s1 = map(int,raw_input().split())
s2 = map(int,raw_input().split())

fl = True

lk = [] 
ls = []
for i in range(l[0]-1):
    lk.append(abs(s1[i]-s1[i+1]))
    ls.append(abs(s2[i]-s2[i+1]))

lk.append(l[1]-s1[-1]+s1[0])
ls.append(l[1]+s2[0]-s2[-1])

fl = False
k = ls[0]
for i in range(len(ls)):
    del(ls[0])
    ls.append(k)
    print(ls)
    k = ls[0]
    if ls == lk:
        fl = True
        break
    
if l[0] == 1:
    print("YES")
elif fl == True:
    print("YES")
else:
    print("NO")
