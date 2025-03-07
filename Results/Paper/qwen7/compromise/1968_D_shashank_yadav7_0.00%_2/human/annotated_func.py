#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each testcase, n, k, P_B, P_S are integers such that 1 ≤ P_B, P_S ≤ n ≤ 2⋅10^5 and 1 ≤ k ≤ 10^9; p is a permutation of length n; a is an array of integers where 1 ≤ a_i ≤ 10^9 for all 1 ≤ i ≤ n.
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
            bm += max(bm, a[b] * k + bp)
            sm += max(sm, a[s] * k + sp)
            sp += a[s]
            bp += a[b]
        
        if bm > sm:
            print('Bodya')
        elif bm < sm:
            print('Sasha')
        else:
            print('Draw')
        
    #State: Output State: After the loop executes all iterations, the variable `i` will be less than `n`, indicating that the loop has completed its execution. The variable `k` will be -1, as it is decremented in each iteration until it reaches 0 and the loop breaks. The variables `b` and `s` will be updated multiple times based on the list `p`, with `b` being updated `n` times and `s` being updated `n-1` times. 
    #
    #The variable `bm` will be the final sum of `bm` and the maximum values calculated during each iteration, considering the updated positions of `b` and `s`. Similarly, `sm` will be the sum of `sm` and the maximum values calculated during each iteration, also considering the updated positions of `b` and `s`. Both `sp` and `bp` will be incremented by the values of `a[s]` and `a[b]` respectively, after each update of `b` and `s`.
    #
    #The final output will be determined by comparing `bm` and `sm`. If `bm` is greater than `sm`, the output will be 'Bodya'. If `sm` is greater than `bm`, the output will be 'Sasha'. If `bm` equals `sm`, the output will be 'Draw'.
    #
    #In summary, the output state will reflect the final values of `bm`, `sm`, `sp`, `bp`, `b`, `s`, `k`, and `i` after the loop completes, along with the final output string based on the comparison between `bm` and `sm`.
#Overall this is what the function does:The function processes a series of test cases, each consisting of integers t, n, k, P_B, P_S, a permutation p, and an array a. For each test case, it updates indices b and s based on the permutation p, calculates two scores bm and sm by iterating through the array a, and compares these scores to determine the winner ('Bodya', 'Sasha', or 'Draw'). The function outputs the result for each test case.

