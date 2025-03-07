#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ k ≤ m ≤ n ≤ 2 × 10^5, representing the lengths of arrays a and b, and the required number of matching elements. Arrays a and b contain integers a_1, a_2, ..., a_n and b_1, b_2, ..., b_m respectively, where 1 ≤ a_i, b_i ≤ 10^6. The sum of n and m over all test cases does not exceed 2 × 10^5.
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
        
    #State: After the loop executes all its iterations, the following changes occur: `fnd` will contain the total number of times `pairs_in_D` was greater than or equal to `k` during the loop's execution. The `D`, `E`, and `C` Counter objects will be updated to their final states, reflecting the last sliding window of `aa` and the entire `bb`. Specifically, `D` will contain the final intersection of the current sliding window with `bb`, `E` will contain the elements in the current sliding window that are not in `D`, and `C` will contain the elements in `bb` that are not in the current sliding window. The `pairs_in_D` will be the final sum of the values in `D`. The values of `n`, `m`, and `k` will remain unchanged, as will the lists `aa` and `bb` and the Counter objects `cnt_aa` and `cnt_bb`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and arrays `a` and `b`. For each test case, it calculates the number of positions in array `a` (from index `m` to `n`) where the number of common elements between the current sliding window of `a` and the entire array `b` is at least `k`. The function prints the count of such positions for each test case. The original arrays `a` and `b`, and the values of `n`, `m`, and `k` remain unchanged after the function execution.

