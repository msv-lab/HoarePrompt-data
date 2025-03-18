#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 × 10^5 and 1 ≤ k ≤ 10^9, representing the length of the permutation, the duration of the game, and the starting positions of Bodya and Sasha, respectively. p is a list of n integers where 1 ≤ p_i ≤ n, representing the permutation p. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the array a. The sum of values of n over all test cases does not exceed 2 × 10^5.
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
        
    #State: The loop has executed `t` times, where `t` is the number of test cases. For each test case, the output is either 'Bodya', 'Sasha', or 'Draw' based on the maximum cumulative scores `maxb` and `maxs` calculated for Bodya and Sasha, respectively. The variables `n`, `k`, `pb`, `ps`, `p`, `a`, `maxa`, `b`, `s`, `founds`, `foundb`, `preb`, `pres`, `sb`, `ss`, `ptsb`, `ptss`, `maxs`, and `maxb` are reset and recalculated for each test case.
#Overall this is what the function does:The function `func` processes a series of test cases. Each test case is defined by the parameters `n`, `k`, `P_B`, and `P_S`, along with two lists `p` and `a`. The function determines the winner of a game between Bodya and Sasha based on the maximum values in the array `a` and the permutations in `p`. The game is played for `k` moves, and the starting positions of Bodya and Sasha are given by `P_B` and `P_S`, respectively. The function prints 'Bodya' if Bodya has the higher cumulative score, 'Sasha' if Sasha has the higher cumulative score, and 'Draw' if their scores are equal. The function does not return any value; it only prints the result for each test case. After processing all test cases, the function concludes.

