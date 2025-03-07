#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5. a is a list of n integers where each element satisfies 1 ≤ a_i ≤ 10^6. b is a list of m integers where each element satisfies 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 · 10^5. The sum of m over all test cases does not exceed 2 · 10^5.
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
        
    #State: After all iterations, `D` is the final intersection of `cnt_aa` and `cnt_bb` after processing all elements, `E` contains adjusted elements from the first `m` elements of `aa`, `C` contains adjusted elements from `bb`, `pairs_in_D` is the final sum of values in `D`, and `fnd` is the count of times `pairs_in_D` was greater than or equal to `k`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers and two integers `n`, `m`, and `k`. For each test case, it calculates how many times a sliding window of size `m` over the first list can have at least `k` common elements with the second list. It outputs the count of such occurrences for each test case.

