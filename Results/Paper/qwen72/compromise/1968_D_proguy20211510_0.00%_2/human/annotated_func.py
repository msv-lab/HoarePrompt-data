#State of the program right berfore the function call: The function `func` is expected to take input parameters, but the function definition provided does not include any. For the problem described, the function should take parameters `t`, `n`, `k`, `P_B`, `P_S`, `p`, and `a`, where `t` is the number of test cases (1 ≤ t ≤ 10^4), `n` is the length of the permutation (1 ≤ n ≤ 2·10^5), `k` is the number of turns in the game (1 ≤ k ≤ 10^9), `P_B` and `P_S` are the starting positions of Bodya and Sasha respectively (1 ≤ P_B, P_S ≤ n), `p` is a permutation of length `n` (1 ≤ p_i ≤ n), and `a` is an array of integers of length `n` (1 ≤ a_i ≤ 10^9). The sum of `n` over all test cases does not exceed 2·10^5.
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
        
    #State: The loop will have completed its execution for all test cases, and the variables `t`, `n`, `k`, `P_B`, `P_S`, `p`, `a`, `maxa`, `b`, `s`, `founds`, `foundb`, `preb`, `pres`, `sb`, `ss`, `ptsb`, `ptss`, `maxs`, and `maxb` will have been updated and used to determine the winner of each game. The final output will be a series of 'Bodya', 'Sasha', or 'Draw' for each test case, based on the conditions provided in the loop. The values of `MOD` and `alpha` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of game scenarios, each defined by the number of test cases `t`, the length of the permutation `n`, the number of turns `k`, the starting positions of two players Bodya (`P_B`) and Sasha (`P_S`), a permutation `p`, and an array of integers `a`. For each test case, the function determines the winner of the game or if it ends in a draw based on the values in `a` and the movement of positions in `p` over `k` turns. The function outputs 'Bodya', 'Sasha', or 'Draw' for each test case, reflecting the final state of the game. The function does not return any values; it only prints the results.

