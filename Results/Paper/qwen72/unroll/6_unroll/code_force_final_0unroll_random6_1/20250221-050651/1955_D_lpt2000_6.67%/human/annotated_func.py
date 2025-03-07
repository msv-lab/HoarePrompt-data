#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n, m, and k are integers such that 1 <= k <= m <= n <= 2 * 10^5, a is a list of n integers where 1 <= a_i <= 10^6, and b is a list of m integers where 1 <= b_i <= 10^6.
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
        
    #State: The loop iterates `nabors` times, and for each iteration, it processes new inputs `n`, `m`, `k`, `aa`, and `bb`. After each iteration, the variables `n`, `m`, `k`, `aa`, and `bb` are updated with new values from the input. The variables `cnt_aa`, `cnt_bb`, `D`, `E`, `C`, `tot`, and `fnd` are recalculated for each iteration. The final output state is that `fnd` is printed for each iteration, representing the number of times the condition `tot >= k` is met during the processing of the lists `aa` and `bb`. The values of `n`, `m`, `k`, `aa`, and `bb` are reset for the next iteration, and the loop continues until all `nabors` iterations are completed.
#Overall this is what the function does:The function `func` reads an integer `nabors` from the input, representing the number of test cases. For each test case, it reads three integers `n`, `m`, and `k` and two lists of integers `aa` and `bb` from the input. It then calculates the number of times a condition is met: the condition is that at least `k` elements from the first `m` elements of `aa` are also present in `bb`. This calculation is performed by sliding a window of size `m` over `aa` and updating the counts of common elements between `aa` and `bb`. The function prints the number of times this condition is met for each test case. After processing all test cases, the function concludes with no return value.

