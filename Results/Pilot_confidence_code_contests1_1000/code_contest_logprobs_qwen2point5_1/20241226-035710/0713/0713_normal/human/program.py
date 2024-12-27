
x=raw_input("")
x1=raw_input("")


x2=[]
for i in range(len(x)):
    if x[i]=="1":
        x2.append(i+1)

res=""

#left=0
#right=0
#k=min(x2)
k1=1

def vybor(x2,left,right,k,res,k1):    
    if left<right:
        for i in range(len(x2)):    
            if x2[i] == k:
                continue
            if (x2[i]+left) > right:
                k=x2[i]                  
                left=left+x2[i]
                res+=str(x2[i])+" "
                k2=1
                break
                
            
            
            

    if left>right:
        for i in range(len(x2)):
            if x2[i] == k:
                continue
            if (x2[i]+right)>left:
                k=x2[i]
                right=right+x2[i]
                res+=str(x2[i])+" "   
                k2=1
                break
                
            
    if k2==0:
        k1=0
            
    return (x2,left,right,k,res,k1)
    
                
                
if len(x2)!=0:        
    
    
    k=min(x2)
    left=k
    right=0
    res+=str(k)+" "
   


    for i in range(int(x1)-1):
        if k1==0:
            break
        x2,left,right,k,res,k1=vybor(x2,left,right,k,res,k1)


if k1==1:    
    print("YES")
    print(res[:-1])

else:
    print("NO")