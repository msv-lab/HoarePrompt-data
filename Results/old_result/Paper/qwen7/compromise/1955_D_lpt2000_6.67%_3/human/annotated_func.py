#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2⋅10^5. a is a list of n integers such that 1 ≤ a_i ≤ 10^6. b is a list of m integers such that 1 ≤ b_i ≤ 10^6. The sum of n over all test cases does not exceed 2⋅10^5, and the sum of m over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: All elements in `D` are set to zero, `C` is empty, `E` contains all unique elements from `aa[:n-m]` that were present in any of the `nabors` iterations, `fnd` is the total number of times the loop executed where `sum(D.values())` was greater than or equal to `k`, `tot` is zero, and `nabors` is decremented by the number of iterations the loop executed.
    #
    #Explanation: After all iterations of the loop, since the loop continuously modifies `D` by decrementing its values and adjusts `C` and `E` based on certain conditions, eventually all values in `D` will be decremented to zero. The variable `fnd` keeps track of the number of times the condition `tot >= k` is met and increments accordingly. The counter `C` will reflect how many times each key's count in `D` matched exactly with its count in `cnt_aa`, and `E` will contain all unique elements from `aa[:n-m]` that were not in `D` after all iterations. The state of `bb`, `cnt_aa`, and `cnt_bb` remains unchanged as they are not modified within the loop. `tot` will be zero because once `D` is empty, no further changes can occur to `tot` which is the sum of `D.values()`. The variable `nabors` is decremented by the number of iterations the loop executed.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \( t \), \( n \), \( m \), \( k \), a list of \( n \) integers \( a \), and a list of \( m \) integers \( b \). For each test case, it calculates the number of times the sum of common elements between the first \( m \) elements of \( a \) and \( b \) is greater than or equal to \( k \). After processing all test cases, it prints the total count of such occurrences. The function updates counters \( D \), \( C \), and \( E \) based on the elements of \( a \) and \( b \) during each iteration, ensuring that \( D \) eventually becomes empty, \( C \) reflects exact matches, and \( E \) contains unique elements from \( a \) not in \( D \).

