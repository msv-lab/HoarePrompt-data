for _ in range(int(input())):
    n = int(input())
    s = input()
    lc,acc = s.count('<'),0
    ans = []
    for i,x in enumerate([i for i in range(n) if s[i] == '<']+[i for i in range(n) if s[i] == '>']):
        if i>=lc:
            ans.append(n-i+acc)
        acc += 2*(x-i)
        if i<lc:
            ans.append(i+1+acc)
    print(*ans) 
            
        


