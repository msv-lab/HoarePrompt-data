#State of the program right berfore the function call: The function `func` is expected to be called within a context that provides the necessary inputs as described in the problem statement, including the number of test cases `t`, the length of the permutation `n`, the duration of the game `k`, the starting positions `P_B` and `P_S`, the permutation `p`, and the array `a`. The inputs are such that 1 ≤ t ≤ 10^4, 1 ≤ P_B, P_S ≤ n ≤ 2 × 10^5, 1 ≤ k ≤ 10^9, 1 ≤ p_i ≤ n, and 1 ≤ a_i ≤ 10^9. The sum of values of `n` over all test cases does not exceed 2 × 10^5.
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
        
    #State: The loop will have processed all the test cases, and for each test case, it will have printed either 'Bodya', 'Sasha', or 'Draw' based on the conditions described in the loop. The variables `n`, `k`, `pb`, `ps`, `p`, `a`, `maxa`, `b`, `s`, `founds`, `foundb`, `preb`, `pres`, `sb`, `ss`, `ptsb`, `ptss`, `maxs`, and `maxb` will have been updated and used within each iteration of the loop, but their final values will depend on the specific inputs for the last test case. The loop control variable `_` will have the value of the number of iterations completed, which is equal to the number of test cases `t`.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the number of elements `n`, the duration of the game `k`, the starting positions of two players `P_B` and `P_S`, a permutation `p`, and an array `a`. For each test case, it determines the outcome of a game where players move according to the permutation and accumulate points based on the array `a`. The function prints 'Bodya', 'Sasha', or 'Draw' for each test case, indicating which player wins or if the game ends in a draw. The final state of the program includes the loop control variable `_` having the value of the number of test cases processed, and the variables `n`, `k`, `pb`, `ps`, `p`, `a`, `maxa`, `b`, `s`, `founds`, `foundb`, `preb`, `pres`, `sb`, `ss`, `ptsb`, `ptss`, `maxs`, and `maxb` being updated and used within each iteration, but their final values depend on the specific inputs of the last test case.

