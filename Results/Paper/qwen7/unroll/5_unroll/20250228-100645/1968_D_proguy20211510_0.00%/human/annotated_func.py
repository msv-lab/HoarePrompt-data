#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2 ⋅ 10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of n integers where 1 ≤ a_i ≤ 10^9.
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
        
    #State: Output State: The output state depends on the inputs provided during each iteration of the loop. The loop processes different inputs for `n`, `k`, `pb`, `ps`, `p`, and `a` in each iteration, and prints either 'Draw', 'Bodya', or 'Sasha' based on the comparison of scores calculated from the lists `b` and `s`. Since the specific inputs are not provided, the exact output state cannot be determined. However, it will consist of a series of 'Draw', 'Bodya', or 'Sasha' outputs corresponding to each iteration's result.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( k \), \( P_B \), and \( P_S \), along with arrays \( p \) and \( a \). For each test case, it determines whether 'Bodya', 'Sasha', or 'Draw' should be printed based on the maximum values in the arrays and their positions. The function iterates through the given inputs, calculates scores for 'Bodya' and 'Sasha', and compares them to decide the winner. If the scores are equal, it prints 'Draw'.

