#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each of the t test cases, n, k, P_B, P_S are integers where 1 ≤ P_B, P_S ≤ n ≤ 2 · 10^5 and 1 ≤ k ≤ 10^9. p is a permutation of length n, and a is an array of length n with elements a_i such that 1 ≤ a_i ≤ 10^9. The sum of values of n over all test cases does not exceed 2 · 10^5.
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
        
    #State: The loop has finished executing all t iterations. For each iteration, the values of `n`, `k`, `b`, `s`, `p`, and `a` are processed, and the final comparison between `bm` and `sm` determines the output, which is either 'Bodya', 'Sasha', or 'Draw'. The values of `t`, `n`, `k`, `b`, `s`, `p`, and `a` remain as they were input, but the loop variables `i`, `bm`, `sm`, `sp`, and `bp` are reset for each new test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by the parameters `n`, `k`, `P_B`, `P_S`, `p`, and `a`. For each test case, it calculates two values, `bm` and `sm`, based on the elements of the permutation `p` and the array `a`. After processing, it compares `bm` and `sm` and prints 'Bodya' if `bm` is greater, 'Sasha' if `sm` is greater, and 'Draw' if they are equal. The function does not return any values but prints the result for each test case. After all test cases are processed, the function concludes, leaving the input parameters unchanged.

