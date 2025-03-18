for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=frozenset(map(int,input().split()))
    b=frozenset(map(int,input().split()))
 
    leftOnes=0
    aOnes=0
    bOnes=0
    newk=k//2
    i=1
    
    while i<=k:
        if i in a and i in b:
            leftOnes+=1
        elif i in a:
            aOnes+=1
        elif i in b:
            bOnes+=1
        else:
            break
        i+=1
 
    i=0
    while i<leftOnes:
        if aOnes<bOnes:
            aOnes+=1
        else:
            bOnes+=1
        i+=1
 
    if aOnes==newk and bOnes==newk:
        print("yes")
    else:
        print("no")