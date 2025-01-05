t = int(input())
while(t):
    n = int(input())
    s = input()
    ans = []
    for i in range(n):
        s_ = s
        t = 0
        b = i
        while(b>=0 and b<=n-1):
            if s_[b]=='>':
                
                s_=s_[:b]+'<'+s_[b+1:]
                b=b+1
            else:
                
                s_=s_[:b]+'>'+s_[b+1:]
                b=b-1
            t=t+1
        ans.append(t)
    print(*ans, sep=" ")
        
    t = t - 1
