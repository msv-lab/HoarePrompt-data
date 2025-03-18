#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, m, and k are integers where 1 ≤ k ≤ m ≤ n ≤ 2 × 10^5, representing the lengths of arrays a and b, and the required number of matching elements, respectively. a is a list of n integers where 1 ≤ a_i ≤ 10^6, and b is a list of m integers where 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 × 10^5, and the sum of m over all test cases does not exceed 2 × 10^5.
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
        
    #State: After all iterations of the loop, the value of `fnd` will be the total count of iterations where `pairs_in_D` was greater than or equal to `k` across all test cases. The values of `D`, `E`, and `C` will reflect the final frequencies of elements after processing all the elements in `aa[m:]` and `aa[:n - m]` for the last test case. The values of `in_aa` and `out_aa` will be the last elements processed in the loop for the last test case. The values of `nabors`, `n`, `m`, `k`, `aa`, `bb`, `cnt_aa`, and `cnt_bb` remain unchanged for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `m`, and `k`, and lists `a` and `b`. For each test case, it calculates the number of times a sliding window of size `m` in list `a` contains at least `k` elements that are also present in list `b`. The function prints the total count of such occurrences for each test case. After processing all test cases, the function ends without returning any value. The final state includes the printed results for each test case, and the internal variables used for computation are reset for each new test case.

