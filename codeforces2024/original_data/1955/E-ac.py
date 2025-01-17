for _ in range(int(input())):
    n = int(input())
    s = input()
    ans = 0
    
    for i in range(n, 0, -1):
        z = -1
        for j in range(i):
            s1 = s[j::i]
            x = sum(1 for k in s1 if k == '0') % 2
            if z != -1 and z != x:
                z = -2
                break
            z = x
        if z != -2:
            ans = i
            break
    
    print(ans)