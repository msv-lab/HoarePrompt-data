#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers such that 1 ≤ a_i ≤ 10^9 for all i.
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
        
    #State: Output State: The output state after the loop executes all iterations is determined by the final values of `maxs` and `maxb`. These values represent the maximum cumulative sums of the points for Sasha (`ptss`) and Bodya (`ptsb`) respectively, considering the contributions from the arrays `b` and `s` up to the last iteration. 
    #
    #The final decision on who wins ('Sasha', 'Bodya', or 'Draw') is made based on the comparison between `maxs` and `maxb`. If `maxs` is greater than `maxb`, Sasha wins. If `maxb` is greater than `maxs`, Bodya wins. If they are equal, it results in a draw.
    #
    #The cumulative sums `preb` and `pres` are calculated for arrays `b` and `s` respectively, and these are used to compute `ptsb` and `ptss` which are then compared to determine the winner. The loop processes up to `k` iterations, updating the positions `pb` and `ps` based on the permutation `p` until the conditions for `founds` and `foundb` are met, or the loop completes its iterations.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( n \), \( k \), \( P_B \), and \( P_S \), a permutation \( p \) of length \( n \), and an array \( a \) of positive integers. For each test case, it determines the winner between Sasha and Bodya based on the values in \( a \) at specific indices and their permutations. If the maximum value in \( a \) is at both specified indices, it prints 'Draw'. Otherwise, it calculates the cumulative sums of points for Sasha and Bodya over \( k \) iterations, considering the permutations and the maximum value in \( a \). Finally, it prints 'Sasha' if her cumulative points are higher, 'Bodya' if his are higher, or 'Draw' if they are equal.

