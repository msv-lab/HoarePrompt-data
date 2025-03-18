num = int(input("Enter number of entries- "))
L1 = []
res = []
for i in range(num):
    L1.append(int(input("Enter entry no."+str(i+1)+"- ")))
for i in range(num):
    for j in range(2,L1[i]+1):
        if(L1[i]%j == 0 ):
            res.append(L1[i]//j*(j-1))
            break
print(*res,sep="\n")