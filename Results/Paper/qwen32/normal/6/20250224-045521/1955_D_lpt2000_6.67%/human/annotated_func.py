#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5. a is a list of n integers where each element a_i satisfies 1 <= a_i <= 10^6. b is a list of m integers where each element b_i satisfies 1 <= b_i <= 10^6. The sum of n over all test cases does not exceed 2 * 10^5. Similarly, the sum of m over all test cases does not exceed 2 * 10^5.
def func():
    nabors = int(input())
    for _ in range(nabors):
        n, m, k = [int(i) for i in input().split()]
        
        aa = [int(i) for i in input().split()]
        
        bb = [int(i) for i in input().split()]
        
        cnt_aa = Counter(aa[:m])
        
        cnt_bb = Counter(bb)
        
        D = cnt_aa & cnt_bb
        
        E = cnt_aa - D
        
        C = cnt_bb - D
        
        tot = sum(D.values())
        
        fnd = 1 if tot >= k else 0
        
        for in_aa, out_aa in zip(aa[m:], aa[:n - m]):
            if D[out_aa] > 0:
                if E[out_aa] > 0:
                    E[out_aa] -= 1
                else:
                    D[out_aa] -= 1
                    C[out_aa] += 1
            else:
                E[out_aa] -= 1
            if C[in_aa] > 0:
                if C[in_aa] == D[in_aa]:
                    C[in_aa] += 1
                else:
                    D[in_aa] += 1
            else:
                E[in_aa] += 1
            tot = sum(D.values())
            fnd += 1 if tot >= k else 0
        
        print(fnd)
        
    #State: the final value of `fnd` after all iterations.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers `n`, `m`, and `k`, and two lists of integers `a` and `b`. For each test case, it calculates how many times a sliding window of size `m` over list `a` contains at least `k` common elements with list `b`. The result for each test case is printed, indicating the count of such occurrences.

