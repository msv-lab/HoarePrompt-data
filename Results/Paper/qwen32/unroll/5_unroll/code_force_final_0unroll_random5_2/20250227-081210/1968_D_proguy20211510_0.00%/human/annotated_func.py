#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each of the t test cases, n, k, P_B, and P_S are positive integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. The permutation p is a list of n integers where each integer is between 1 and n, inclusive, and the array a is a list of n integers where each integer is between 1 and 10^9, inclusive. The sum of values of n over all test cases does not exceed 2 * 10^5.
def func():
    YES, NO = 'YES', 'NO'
    MOD = 10 ** 9 + 7
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for _ in range(int(input())):
        n, k, pb, ps = input().split()
        
        n, k, pb, ps = int(n), int(k), int(pb), int(ps)
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        maxa = max(a)
        
        if a[pb - 1] == a[ps - 1] == maxa:
            print('Draw')
            continue
        elif a[pb - 1] == maxa:
            print('Bodya')
            continue
        elif a[ps - 1] == maxa:
            print('Sasha')
            continue
        
        b, s = [], []
        
        founds, foundb = False, False
        
        for i in range(k):
            if foundb and founds:
                b.append((k - (i + 1)) * maxa)
                s.append((k - (i + 1)) * maxa)
                break
            if foundb:
                b.append(maxa)
            elif a[pb - 1] == maxa:
                foundb = True
                b.append(a[pb - 1])
            else:
                b.append(a[pb - 1])
                pb = p[pb - 1]
            if founds:
                s.append(maxa)
            elif a[ps - 1] == maxa:
                founds = True
                s.append(a[ps - 1])
            else:
                s.append(a[ps - 1])
                ps = p[ps - 1]
        
        preb, pres = [], []
        
        sb, ss = 0, 0
        
        for i in range(len(s)):
            preb.append(sb + b[i])
            sb += b[i]
            pres.append(ss + s[i])
            ss += s[i]
        
        ptsb, ptss = [], []
        
        for i in range(len(pres)):
            rem = k - (i + 1)
            ptsb.append(preb[i] + rem * b[i])
            ptss.append(pres[i] + rem * s[i])
        
        maxs, maxb = max(ptss), max(ptsb)
        
        if maxs > maxb:
            print('Sasha')
        elif maxs < maxb:
            print('Bodya')
        else:
            print('Draw')
        
    #State: A list of "Bodya", "Sasha", or "Draw" for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers `n`, `k`, `P_B`, and `P_S`, and two lists: a permutation `p` and an array `a`. For each test case, it determines the winner between "Bodya" and "Sasha" based on the values in `a` and the permutation `p`, or declares a "Draw" if the outcome is tied. The function outputs "Bodya", "Sasha", or "Draw" for each test case.

