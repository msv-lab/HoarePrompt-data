#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 ⋅ 10^5. a is a list of n integers where 1 ≤ a_i ≤ 10^6 for all 1 ≤ i ≤ n. b is a list of m integers where 1 ≤ b_i ≤ 10^6 for all 1 ≤ i ≤ m. The sum of n over all test cases does not exceed 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State: The value of `fnd` after executing the loop for `nabors` iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it takes integers t, n, m, k, a (a list of n integers), and b (a list of m integers) as inputs. It calculates the number of test cases (fnd) for which the count of common elements between the first m elements of list a and list b is greater than or equal to k. After processing all test cases, it prints the total count of such test cases.

