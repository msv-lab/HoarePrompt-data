#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2⋅10^5. a is a list of n integers where each element is between 1 and 10^6 inclusive. b is a list of m integers where each element is between 1 and 10^6 inclusive. The sum of n over all test cases does not exceed 2⋅10^5, and the sum of m over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `fnd` is the count of iterations where the sum of values in dictionary `D` is greater than or equal to `k`.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes integers \( t \), \( n \), \( m \), and \( k \), and lists \( a \) and \( b \). It calculates the count of iterations where the sum of values in dictionary \( D \) (which represents the intersection of counters \( cnt\_aa \) and \( cnt\_bb \)) is greater than or equal to \( k \). Finally, it prints the total count of such iterations for all test cases.

