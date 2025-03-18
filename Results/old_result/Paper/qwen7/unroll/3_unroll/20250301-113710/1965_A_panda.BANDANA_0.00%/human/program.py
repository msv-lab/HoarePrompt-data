t=int(input())
for  i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    e=set(l)
    m=len(l)
 
    if  1 in l:
        print("Bob" )
    else:
        print("Alice" )