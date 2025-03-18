#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that k ≤ n ≤ 10^9, k is an integer such that 1 ≤ k ≤ 10^5, and q is an integer such that 1 ≤ q ≤ 10^5. a is a list of k integers where 1 ≤ a_i ≤ n, a_i < a_{i+1} for every 1 ≤ i ≤ k-1, and a_k = n. b is a list of k integers where 1 ≤ b_i ≤ 10^9, b_i < b_{i+1} for every 1 ≤ i ≤ k-1. There are q queries, each query being an integer d such that 0 ≤ d ≤ n. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
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
        
    #State: All test cases have been processed, and for each test case, all queries have been answered. The variables `t`, `n`, `k`, `q`, `a`, `b`, `ad`, `bd`, and `v` reflect the current test case's data, while `l` is `-1` indicating no more queries are left in the current test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two lists of integers `a` and `b`, and a series of queries. For each query `d`, it calculates and prints an integer value based on the relationship between the lists `a` and `b`. Specifically, it determines a value `m` such that if `d` matches an element in `a`, `m` is the corresponding element in `b`; otherwise, `m` is interpolated based on the differences between consecutive elements in `a` and `b`. After processing all queries for a test case, it moves on to the next test case until all test cases are completed.

