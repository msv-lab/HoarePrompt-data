#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are positive integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of positive integers such that 1 ≤ a_i ≤ 10^9 for all i.
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
        
    #State: Output State: The output state depends on the input values for each iteration of the loop. For each input, the program compares the maximum possible scores for 'Bodya' and 'Sasha' based on the given rules and prints 'Bodya', 'Sasha', or 'Draw' accordingly. After all iterations, the final printed result for each iteration is part of the output state.
#Overall this is what the function does:The function processes multiple test cases, where for each case, it reads in values for \( t \), \( n \), \( k \), \( b \), \( s \), a permutation \( p \), and an array \( a \). It then calculates the maximum possible scores for two players, 'Bodya' and 'Sasha', based on the given rules. Finally, it prints 'Bodya', 'Sasha', or 'Draw' depending on which player has the higher score. After processing all test cases, it outputs the results for each case.

