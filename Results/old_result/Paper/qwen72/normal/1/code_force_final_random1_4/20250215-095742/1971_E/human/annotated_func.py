#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and q are integers where k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, representing the final destination, the number of known time points, and the number of queries, respectively. a is a list of k integers where 1 ≤ a_i ≤ n and a_i < a_{i+1} for every 1 ≤ i ≤ k-1, with a_k = n. b is a list of k integers where 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. Each query d is an integer where 0 ≤ d ≤ n. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, k, q = map(int, input().split())
        
        a = [0] + list(map(int, input().split()))
        
        b = [0] + list(map(int, input().split()))
        
        ad = [0]
        
        bd = [0]
        
        for i in range(1, len(a)):
            ad.append(a[i] - a[i - 1])
        
        for i in range(1, len(b)):
            bd.append(b[i] - b[i - 1])
        
        v = [0]
        
        for i in range(1, len(a)):
            v.append(ad[i] / bd[i])
        
        for l in range(q):
            m = 0
            i = 1
            ql = int(input())
            s = bisect_left(a, ql)
            if a[s] == ql:
                print(b[s], end=' ')
                continue
            ql -= a[s - 1]
            m += b[s - 1]
            m += bd[s] * ql / ad[s]
            print(int(m), end=' ')
        
        print()
        
    #State: After the loop executes all the iterations, `t` is 0, `n`, `k`, `q`, `a`, `b`, `ad`, `bd`, and `v` remain unchanged for each test case. `l` is 0, `m` is the final calculated value based on the last `ql` input, `i` is 1, `ql` is the last input value minus the appropriate `a[s - 1]`, and `s` is the index where the last `ql` would fit in the list `a` to maintain sorted order.
#Overall this is what the function does:The function `func` processes a series of test cases, each defined by a final destination `n`, the number of known time points `k`, the number of queries `q`, and two lists `a` and `b` representing known positions and times, respectively. For each query `d`, the function calculates and prints the time corresponding to the position `d` based on the known positions and times. After processing all test cases, the function leaves the input variables `t`, `n`, `k`, `q`, `a`, `b`, `ad`, `bd`, and `v` unchanged, while the internal variables used for calculations (`l`, `m`, `i`, `ql`, `s`) are reset or updated for each test case.

