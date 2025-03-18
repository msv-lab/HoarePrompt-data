#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers such that 1 <= p_i <= n. a is a list of n integers such that 1 <= a_i <= 10^9. The sum of values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: For each testcase, the output will be either 'Bodya', 'Sasha', or 'Draw' based on the comparison of `bm` and `sm` after the loop completes. The values of `t`, `n`, `k`, `b`, `s`, `p`, and `a` will remain unchanged from their input values, but `bm` and `sm` will be the final sums calculated in the loop.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `P_B`, and `P_S`, along with two lists `p` and `a`. For each test case, it calculates two sums based on the values in `a` and the indices in `p`, adjusted by `k`. It then compares these sums and prints 'Bodya' if the first sum is greater, 'Sasha' if the second sum is greater, or 'Draw' if they are equal. The function does not modify the input values but outputs a result for each test case.

