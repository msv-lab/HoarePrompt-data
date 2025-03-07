#State of the program right berfore the function call: The function should take three parameters: n, m, and k, where n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5. Additionally, it should take two lists of integers, a and b, where a has n elements and b has m elements, and each element in a and b is an integer in the range 1 ≤ a_i, b_i ≤ 10^6.
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
        
    #State: The loop has completed all iterations, and the final state of the variables is as follows: `n` and `m` remain unchanged, `aa` and `bb` remain unchanged, `D` contains the updated frequencies of elements that are common between the first `m` elements of `aa` and `bb` after all iterations, `C` contains the updated frequencies of elements in `bb` that are not in `D` after all iterations, `E` contains the updated frequencies of elements in the first `m` elements of `aa` that are not in `D` after all iterations, `tot` is the sum of all values in `D`, and `fnd` is the total number of times `tot` was greater than or equal to `k` during the loop's execution. `nabors` is 0.
#Overall this is what the function does:The function `func` reads an integer `nabors` from the input, which indicates the number of test cases to process. For each test case, it reads three integers `n`, `m`, and `k` and two lists of integers `aa` and `bb`. The function then calculates the number of times a specific condition is met during the processing of each test case. Specifically, it counts how many times the number of common elements between the first `m` elements of `aa` and `bb` is greater than or equal to `k` after processing all elements of `aa`. The function prints the count for each test case. The function does not return any value. After the function concludes, `nabors` is 0, and the input lists `aa` and `bb` remain unchanged.

