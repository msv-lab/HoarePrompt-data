#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5. The array a contains n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^6. The array b contains m integers b_1, b_2, ..., b_m where 1 ≤ b_i ≤ 10^6. The sum of n and the sum of m over all test cases do not exceed 2 · 10^5.
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
        
    #State: The variable `fnd` will contain the number of times the condition `pairs_in_D >= k` is true during the execution of the loop. The arrays `aa` and `bb` will remain unchanged. The variables `cnt_aa`, `cnt_bb`, `D`, `E`, and `C` will be updated based on the operations within the loop, but their final states are not explicitly defined in the output. The variables `n`, `m`, and `k` will be overwritten in each iteration of the loop, but their final values will be the last input values read.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `m`, and `k`, and two arrays `a` and `b`. For each test case, it calculates the number of times the condition `pairs_in_D >= k` is true, where `pairs_in_D` represents the number of common elements between the first `m` elements of `a` and the elements of `b`. The function prints this count for each test case. The arrays `a` and `b` remain unchanged throughout the function execution. The variables `cnt_aa`, `cnt_bb`, `D`, `E`, and `C` are used internally to track the counts and intersections of elements, but their final states are not relevant to the output. The variables `n`, `m`, and `k` are overwritten in each iteration of the loop, and their final values will be the last input values read.

