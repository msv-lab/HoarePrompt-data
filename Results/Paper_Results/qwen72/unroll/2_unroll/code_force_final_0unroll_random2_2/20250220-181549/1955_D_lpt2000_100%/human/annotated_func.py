#State of the program right berfore the function call: The function should take three parameters: a list of integers `a`, a list of integers `b`, and an integer `k`. `a` has length `n`, `b` has length `m`, and `k` is an integer such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5. Each element in `a` and `b` is an integer in the range 1 ≤ a_i, b_i ≤ 10^6. The function should also handle multiple test cases, indicated by an integer `t` where 1 ≤ t ≤ 10^4.
def func():
    nabors = int(input())
    for _ in range(nabors):
        n, m, k = [int(i) for i in input().split()]
        
        aa = [str(i) for i in input().split()]
        
        bb = [str(i) for i in input().split()]
        
        cnt_aa = Counter(aa[:m])
        
        cnt_bb = Counter(bb)
        
        D = cnt_aa & cnt_bb
        
        pairs_in_D = sum(D.values())
        
        E = cnt_aa - D
        
        C = cnt_bb - D
        
        fnd = 1 if pairs_in_D >= k else 0
        
        for in_aa, out_aa in zip(aa[m:], aa[:n - m]):
            if D[out_aa] > 0:
                if E[out_aa] > 0:
                    E[out_aa] -= 1
                else:
                    D[out_aa] -= 1
                    pairs_in_D -= 1
                    C[out_aa] += 1
            else:
                E[out_aa] -= 1
            if C[in_aa] > 0:
                D[in_aa] += 1
                pairs_in_D += 1
                C[in_aa] -= 1
            else:
                E[in_aa] += 1
            fnd += 1 if pairs_in_D >= k else 0
        
        print(fnd)
        
    #State: The variable `fnd` contains the total number of times the number of common elements between the first `m` elements of `aa` and `bb` was greater than or equal to `k` during the entire process of sliding the window of size `m` over the list `aa`. The variables `n`, `m`, `k`, `aa`, `bb`, `cnt_aa`, `cnt_bb`, `D`, `pairs_in_D`, `E`, and `C` are updated as the loop processes each test case, but their final values depend on the specific input and the number of iterations.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it takes three integers `n`, `m`, and `k`, followed by two lists of integers `aa` and `bb` of lengths `n` and `m` respectively. It then calculates the number of times the number of common elements between the first `m` elements of `aa` and the elements of `bb` is greater than or equal to `k` as a sliding window of size `m` moves over `aa`. The function prints the total count of such occurrences for each test case. The function does not return any value; it only prints the results to the standard output.

