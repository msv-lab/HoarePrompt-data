#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n, k, P_B, P_S are integers where 1 ≤ P_B, P_S ≤ n ≤ 2 × 10^5 and 1 ≤ k ≤ 10^9. p is a permutation of length n, and a is an array of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: For each of the t test cases, the loop will print either 'Bodya', 'Sasha', or 'Draw' based on the conditions within the loop. The variables `n`, `k`, `pb`, `ps`, `p`, `a`, `maxa`, `b`, `s`, `preb`, `pres`, `ptsb`, `ptss`, `maxs`, `maxb`, `sb`, `ss`, `founds`, and `foundb` will be updated and used within the loop, but their final values will not be relevant outside of the loop. The loop will execute t times, and the output for each test case will be determined by the conditions specified in the loop.
#Overall this is what the function does:The function processes `t` test cases, where each test case involves integers `n`, `k`, `P_B`, `P_S`, a permutation `p` of length `n`, and an array `a` of `n` positive integers. For each test case, it determines and prints the winner ('Bodya' or 'Sasha') or if it's a 'Draw' based on the maximum value in `a` and the positions `P_B` and `P_S` within `p`. The function does not return any value, but it prints the result for each test case. After processing all test cases, the function concludes, and the final state of the program is determined by the printed results.

