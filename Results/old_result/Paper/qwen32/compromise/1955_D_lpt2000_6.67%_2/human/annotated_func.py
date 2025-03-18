#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5, a is a list of n integers where each integer is in the range 1 to 10^6, and b is a list of m integers where each integer is in the range 1 to 10^6. The sum of n over all test cases does not exceed 2 * 10^5, and the sum of m over all test cases does not exceed 2 * 10^5.
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
        
    #State: t is unchanged, nabors is 0, n and m are unchanged, aa and bb are unchanged, cnt_aa and cnt_bb are unchanged, D, E, and C are updated based on the loop's logic, tot is the sum of the values in D after all iterations, fnd is the total number of times tot >= k during all iterations.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it determines how many times a sliding window of size `m` over list `a` can contain at least `k` common elements with list `b`. It prints the count of such occurrences for each test case.

