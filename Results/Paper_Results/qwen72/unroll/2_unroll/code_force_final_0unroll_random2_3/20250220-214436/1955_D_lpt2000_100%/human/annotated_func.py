#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n, m, and k are integers such that 1 ≤ k ≤ m ≤ n ≤ 2 · 10^5, and a and b are lists of integers where a has n elements and b has m elements, and 1 ≤ a_i, b_i ≤ 10^6 for all i.
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
        
    #State: The loop iterates `nabors` times, and for each iteration, it reads new values for `n`, `m`, and `k`, and new lists `aa` and `bb`. After processing these inputs, it prints the number of times the condition `pairs_in_D >= k` is true during the iteration. The variables `n`, `m`, `k`, `aa`, `bb`, `cnt_aa`, `cnt_bb`, `D`, `pairs_in_D`, `E`, `C`, and `fnd` are updated and reset for each iteration. The initial state of `t` remains unchanged.
#Overall this is what the function does:The function `func` reads an integer `t` indicating the number of test cases. For each test case, it reads three integers `n`, `m`, and `k`, and two lists of integers `aa` and `bb` of lengths `n` and `m` respectively. The function then processes these inputs to determine how many times the number of common elements between the first `m` elements of `aa` and `bb` is at least `k` as the window of `m` elements in `aa` slides from the beginning to the end of the list. The result for each test case is printed to the console. The function does not return any value; it only prints the results. The initial state of `t` remains unchanged, and the function processes each test case independently, resetting all internal variables for each new test case.

