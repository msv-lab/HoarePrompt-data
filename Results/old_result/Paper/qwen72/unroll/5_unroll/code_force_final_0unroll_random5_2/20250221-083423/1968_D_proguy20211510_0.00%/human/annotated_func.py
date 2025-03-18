#State of the program right berfore the function call: The function `func` is not properly defined to match the problem description. The function should take parameters for the number of test cases `t`, the length of the permutation `n`, the duration of the game `k`, the starting positions of Bodya `P_B` and Sasha `P_S`, the permutation `p`, and the array `a`.
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
        
    #State: The loop processes each test case, updating the starting positions `pb` and `ps` as well as the arrays `b` and `s` for each iteration. After all iterations, the loop prints 'Bodya', 'Sasha', or 'Draw' based on the maximum scores calculated for Bodya and Sasha. The variables `n`, `k`, `pb`, `ps`, `p`, and `a` are reset for each new test case, and the loop continues to the next test case until all test cases are processed.
#Overall this is what the function does:The function `func` processes multiple test cases, each involving a game between Bodya and Sasha. It takes inputs for the number of test cases, the length of the permutation, the duration of the game, the starting positions of Bodya and Sasha, the permutation, and an array of values. For each test case, it determines the winner of the game based on the maximum values in the array and the movement of Bodya and Sasha according to the permutation. The function prints 'Bodya', 'Sasha', or 'Draw' for each test case, indicating the winner or if the game ends in a draw. The function does not return any values; it only prints the results.

