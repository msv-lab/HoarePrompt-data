t=int(input())
li=[int(x) for x in raw_input().split()]
flag=0
maxi=0
if li[0]==0 and t!=1:    
     for x in range(1,t):
         if li[x]>maxi and li[x]!=maxi+1:
             print((x+1))
             flag=1
             break
         maxi=max(maxi,li[x])
     if flag==0:
        print("-1")
else:
    if t==1 and li[0]==0:
        print("-1")
    else:    
        print("1")
        
    