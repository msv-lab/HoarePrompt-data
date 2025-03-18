t=int(input())
 
for i in range(t):
    n=int(input())
    a=input()
    count=a.count('1')
 
    if count==0:
        print("YES")
 
    elif count>2 and count%2==0:
        print("YES")
 
    elif count==2:
        if a.index('1') and a[a.index('1')+1]!='1':
            print("YES")
        
        else:
            print("NO")
    else:
        print("NO")