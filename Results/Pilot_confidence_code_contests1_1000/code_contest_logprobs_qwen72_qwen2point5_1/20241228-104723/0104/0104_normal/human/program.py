n=int(raw_input())
def mcd(a,b):
    if b==0:
        return a
    else:
        return mcd(b,a%b)
if n==1:
    print(1)
elif n==2:
    print(2)
else:
    ans=n
    sec=0
    count=0
    for i in range(n-1,1,-1):
        if (count==0):
            if(mcd(n,i)==1):
                ans*=i
                sec=i
                count+=1
        elif (count==1):
            if(mcd(n,i)==1 and mcd(sec,i)==1):
                ans*=i
                count+=1
        elif(count==2):
            break
    print(ans)
