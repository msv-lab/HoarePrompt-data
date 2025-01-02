n=int(raw_input())
str=raw_input()
l=[int(e) for e in str.split()]
odd=[]
even=[]
for e in l:
    if e%2==0:
        even=even+[e]
    else:
        odd=odd+[e]
l1=len(odd)
l2=len(even)
odd.sort()
even.sort()
ans=0
if(len(even)>len(odd)):
    temp=len(even)-len(odd)
    ans=sum(even[0:temp-1])
if(len(even)<len(odd)):
    temp=-len(even)+len(odd)
    ans=sum(odd[0:temp-1])
print(ans)

