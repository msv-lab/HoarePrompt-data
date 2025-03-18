#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and q are integers where k ≤ n ≤ 10^9 and 1 ≤ k, q ≤ 10^5, representing the final destination, the number of known time points, and the number of queries, respectively. a is a list of k integers where 1 ≤ a_i ≤ n and a_i < a_{i+1} for every 1 ≤ i ≤ k-1, with a_k = n. b is a list of k integers where 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. Each query d is an integer where 0 ≤ d ≤ n. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
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
        
    #State: After all iterations of the loop, `l` is equal to `q - 1`, `m` is the final calculated value based on the formula `b[s - 1] + bd[s] * (ql - a[s - 1]) / ad[s]` for the last iteration, `ql` is the final adjusted value after subtracting `a[s - 1]` for the last iteration, `s` is the index of the first element in `a` that is not less than the original `ql` for the last iteration, and all other variables (`t`, `n`, `k`, `a`, `b`, `ad`, `bd`, `v`, `i`) remain unchanged from their initial states.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `k`, and `q`, and lists `a` and `b`. For each test case, it reads the values of `n`, `k`, and `q`, followed by the lists `a` and `b`. It then processes `q` queries, where each query `d` is an integer. For each query, the function calculates and prints the time it takes to reach position `d` based on the known positions and times stored in `a` and `b`. The function prints the results of each query separated by spaces, and each test case's results are printed on a new line. After processing all test cases, the function completes, and all input variables (`t`, `n`, `k`, `a`, `b`, `q`, etc.) retain their final states from the last test case.

