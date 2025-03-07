#State of the program right berfore the function call: The function `func` is expected to take input through a predefined structure, such as reading from standard input, which includes the number of test cases t (1 ≤ t ≤ 10^4), for each test case the integers n, k, P_B, P_S (1 ≤ P_B, P_S ≤ n ≤ 2·10^5, 1 ≤ k ≤ 10^9), a permutation p of length n (1 ≤ p_i ≤ n), and an array a of length n (1 ≤ a_i ≤ 10^9). The sum of values of n over all test cases does not exceed 2·10^5.
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
        
    #State: The function `func` will have processed all test cases and printed the result ('Bodya', 'Sasha', or 'Draw') for each test case. The variables `n`, `k`, `pb`, `ps`, `p`, `a`, `maxa`, `b`, `s`, `preb`, `pres`, `sb`, `ss`, `ptsb`, `ptss`, `maxs`, and `maxb` will have been updated and used during the loop execution, but their final values will be irrelevant as they are reset for each test case. The loop will have completed all iterations, and the function will have finished executing.
#Overall this is what the function does:The function `func` reads multiple test cases from standard input, each consisting of integers `n`, `k`, `P_B`, `P_S`, a permutation `p` of length `n`, and an array `a` of length `n`. For each test case, it determines the winner of a game between two players, Bodya and Sasha, based on the maximum value in `a` and the positions `P_B` and `P_S`. The function prints 'Bodya' if Bodya wins, 'Sasha' if Sasha wins, or 'Draw' if the game is a draw. After processing all test cases, the function completes and the final state of the program is that all test cases have been evaluated and the results have been printed.

