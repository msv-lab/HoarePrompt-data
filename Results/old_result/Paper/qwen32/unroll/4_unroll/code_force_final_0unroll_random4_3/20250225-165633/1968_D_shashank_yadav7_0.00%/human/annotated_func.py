#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each testcase, n, k, P_B, and P_S are integers such that 1 <= P_B, P_S <= n <= 2 * 10^5 and 1 <= k <= 10^9. p is a list of n integers where each integer is between 1 and n inclusive. a is a list of n integers where each integer is between 1 and 10^9 inclusive. The sum of values of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The output state after all the iterations of the loop will be a series of strings ("Bodya", "Sasha", or "Draw") printed for each test case, based on the comparison of `bm` and `sm` after processing all the iterations for that test case.
    #
    #Since the problem does not specify the exact input values, we cannot provide a specific numerical output state. However, we can describe the state in terms of the output strings that will be printed.
    #
    #Output State:
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `k`, `P_B`, and `P_S`, and lists `p` and `a`. For each test case, it calculates two scores, `bm` and `sm`, based on the values in `p` and `a`, and prints "Bodya" if `bm` is greater than `sm`, "Sasha" if `sm` is greater than `bm`, or "Draw" if they are equal.

