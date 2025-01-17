n=int(input())
for _ in range(3):
    nm=input().split()
    s=input()
    n,m=int(nm[0]),int(nm[1])
    x=0
    y='ABCDEFG'
    for i in y:
        z=s.count(i)
        if z<m:
            x+=m-z
    print(x)