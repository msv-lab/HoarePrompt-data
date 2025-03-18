#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 ⋅ 10^5. a is a list of n integers such that 1 ≤ a_i ≤ 10^6. b is a list of m integers such that 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: All elements in `aa` and `bb` have been fully processed. `fnd` is incremented by 1 for every iteration where `tot` (the sum of `D.values()`) is greater than or equal to `k`. `D` contains the final counts of elements that were common between `aa[:m]` and `bb`, adjusted by the loop's operations. `C` reflects the counts of elements in `aa[m:]` that were not in `bb`, with these counts incremented based on the loop's logic. `E` shows the net changes in counts of elements in `aa[:n-m]` that were also in `bb`. `tot` is the sum of the values in `D` after all iterations. `nabors` is decremented by the number of iterations, and `aa` and `bb` are updated to new lists of integers as per the input provided.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of integers \( t \), \( n \), \( m \), and \( k \), along with two lists of integers \( a \) and \( b \). For each test case, it calculates the number of times the sum of the counts of common elements between the first \( m \) elements of \( a \) and \( b \) meets or exceeds \( k \) after processing all elements of \( a \) and \( b \). The function returns the total count of such occurrences across all test cases.

