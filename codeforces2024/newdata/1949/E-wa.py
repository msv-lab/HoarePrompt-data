n,k=map(int,input().split(' '))
arr= list(map(int,input().split(' ')))
kk=k//2

if kk*2!=k:
    flag =True
    for x in arr:
        flag= x%(kk+1)!=0 and flag
    if not flag: 
        kk+=1
print(f"{kk} {k-kk}")
         