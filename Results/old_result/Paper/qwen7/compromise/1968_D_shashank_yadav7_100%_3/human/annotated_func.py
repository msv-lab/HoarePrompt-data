#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each test case, n, k, P_B, and P_S are integers satisfying 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers of length n.
def func():
    t = int(input())
    for i in range(t):
        n, k, b, s = list(map(int, input().split()))
        
        p = list(map(int, input().split()))
        
        a = list(map(int, input().split()))
        
        b -= 1
        
        s -= 1
        
        sp = a[s]
        
        bp = a[b]
        
        bm = a[b] * k
        
        sm = a[s] * k
        
        for i in range(n):
            k -= 1
            if k == 0:
                break
            b = p[b] - 1
            s = p[s] - 1
            bm = max(bm, a[b] * k + bp)
            sm = max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: After the loop executes all iterations, `i` will equal `t-1`, `k` will be 0, `b` will be `p[p[...p[b]...-1]-1] - (n-1)`, `s` will be `p[p[...p[s]...-1] - (n-2)`, `bm` will be the maximum value accumulated from the expression `a[b] * k + bp` during each iteration, `sm` will be the maximum value accumulated from the expression `a[s] * k + sp` during each iteration, `sp` will be the sum of `a[s]` for all iterations, `bp` will be the sum of `a[b]` for all iterations, and the final comparison will be made between `bm` and `sm` to decide whether to print 'Bodya', 'Sasha', or 'Draw'.
#Overall this is what the function does:The function processes multiple test cases, each defined by a positive integer \( t \), and for each test case, it reads values for \( n \), \( k \), \( b \), and \( s \). It then takes a permutation \( p \) and an array \( a \) as inputs. The function calculates two values, \( bm \) and \( sm \), by iterating through the permutation and updating based on the values in the array \( a \). Finally, it compares \( bm \) and \( sm \) and prints either "Bodya", "Sasha", or "Draw" based on their comparison.

