q=int(input())
mn=100
for i in range(q):
    
    a,b,c=map(int,input().split())
    if a<b<c:
        print("STAIR")
    if a<b>c:
        print("PEAK")
    else:
        print("NONE")