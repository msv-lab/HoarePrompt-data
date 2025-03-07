#State of the program right berfore the function call: t is a positive integer, and for each test case, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 \cdot 10^5 and 1 ≤ k ≤ 10^9. Additionally, p is a permutation of length n, and a is an array of positive integers.
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
        
    #State: Output State: The loop will execute based on the input provided, and after all iterations, the final output state will be determined by the maximum value between `maxs` and `maxb`. Specifically, if `maxs` (the maximum value in `ptss`) is greater than `maxb` (the maximum value in `ptsb`), then "Sasha" will be printed. Otherwise, if `maxs` is not greater than `maxb`, "Bodya" will be printed. If `maxs` and `maxb` are equal, the output will be "Draw".
    #
    #This final output state is derived from the cumulative sums and comparisons made within the loop for each iteration, with `maxs` and `maxb` being updated based on the conditions specified in the loop body.
#Overall this is what the function does:The function processes multiple test cases, each defined by values of \(n\), \(k\), \(P_B\), \(P_S\), a permutation \(p\), and an array \(a\). For each test case, it determines the winner between Sasha and Bodya based on the values in \(a\) at indices \(P_B-1\) and \(P_S-1\). If these values are equal to the maximum value in \(a\), it prints "Draw". Otherwise, it calculates scores for both Sasha and Bodya over \(k\) rounds, updating the scores based on the maximum value in \(a\) and the permutation \(p\). Finally, it prints "Sasha" if her score is higher, "Bodya" if his score is higher, or "Draw" if their scores are equal.

