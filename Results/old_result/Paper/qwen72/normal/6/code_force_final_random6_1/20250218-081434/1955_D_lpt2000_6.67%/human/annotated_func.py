#State of the program right berfore the function call: t is an integer such that 1 \le t \le 10^4. For each test case, n, m, and k are integers such that 1 \le k \le m \le n \le 2 \cdot 10^5. a is a list of n integers where 1 \le a_i \le 10^6. b is a list of m integers where 1 \le b_i \le 10^6. The sum of n over all test cases does not exceed 2 \cdot 10^5, and the sum of m over all test cases does not exceed 2 \cdot 10^5.
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
        
    #State: After all iterations of the loop, `tot` is the final sum of the values in `D`, `fnd` is the total number of times `tot` was greater than or equal to `k` during the entire loop execution, `in_aa` is the last element of `aa[m:]`, `out_aa` is the last element of `aa[:n - m]`, `D` is the final intersection of `cnt_aa` and `cnt_bb`, `E` is the final Counter object containing the elements of the first `m` elements of `aa` that are not in `D`, and `C` is the final Counter object containing the elements of `bb` that are not in `D`. The values of `cnt_bb`, `cnt_aa`, `n`, `m`, `k`, `t`, `a`, `b`, `nabors`, `aa`, and `bb` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads the number of elements `n`, the window size `m`, and the threshold `k`, followed by two lists of integers `aa` and `bb`. It calculates the number of times a sliding window of size `m` in `aa` contains at least `k` elements that are also in `bb`. The function prints the count of such occurrences for each test case. The function does not return any value; it only prints the results. After the function concludes, the state of the program includes the final count of valid windows (`fnd`), the final intersection of elements (`D`), and the final counts of elements in `aa` and `bb` that are not in the intersection (`E` and `C` respectively). The original input values and lists remain unchanged.

