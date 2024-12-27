t=int(raw_input())
for _ in range(t):
    x=int(raw_input())
    l=1
    ans=1
    sm=1
    for i in range(2,10^6):
        l=2*l+1
        sm+=(l*(l+1))/2
        if sm>x:
            break
    print(i-1)