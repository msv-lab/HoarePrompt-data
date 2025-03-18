#State of the program right berfore the function call: t is a positive integer, and for each test case, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9. Additionally, p is a permutation of length n, and a is an array of positive integers of length n.
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
        
    #State: The loop has executed all its iterations, and the final output depends on the comparison between the maximum values in `ptss` and `ptsb`. If `maxs` (the maximum value in `ptss`) is greater than `maxb` (the maximum value in `ptsb`), then `maxs` remains the maximum value in `ptss`. Otherwise, `maxb` remains the maximum value between `maxb` and `maxs`. The value of `i` is `k + len(pres) - 1`, and `rem` is `k - (i + 1)`.
#Overall this is what the function does:The function processes a series of test cases, each defined by positive integers \( n \), \( k \), \( P_B \), and \( P_S \), along with arrays \( p \) and \( a \). For each test case, it determines whether "Bodya", "Sasha", or "Draw" based on the values in array \( a \) at positions \( P_B - 1 \) and \( P_S - 1 \), and their permutations. It calculates scores for "Bodya" and "Sasha" using permutations and comparisons, and outputs the result of the comparison between these scores.

