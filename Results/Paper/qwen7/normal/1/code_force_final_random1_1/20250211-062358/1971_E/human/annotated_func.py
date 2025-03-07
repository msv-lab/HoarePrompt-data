#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and q are integers such that k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, and the sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5. a is a list of k integers where 1 ≤ a_i ≤ n and a_i < a_{i+1} for every 1 ≤ i ≤ k-1, and a_k = n. b is a list of k integers where 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. d is a list of q integers where 0 ≤ d ≤ n.
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
        
    #State: Output State: All the variables `i`, `l`, `m`, `ql`, and `s` will reflect their final values after the loop has completed all its iterations. Specifically:
    #
    #- `i` will be `len(a) + 1`, as it starts from 1 and increments with each iteration until it reaches the length of `a`.
    #- `l` will be `q + (len(a) - 1)`, indicating the total number of queries processed across all test cases.
    #- `m` will be the cumulative sum of interpolated values calculated for each query within the context of the last test case.
    #- `ql` will be the final input integer reduced by the cumulative sum of elements in `a` up to the point where the last query was satisfied.
    #- `s` will be the index determined by `bisect_left(a, ql)` for the last query processed.
    #
    #This state reflects the completion of the loop after processing all test cases and queries, with all relevant variables updated to their final values based on the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers \(n\), \(k\), and \(q\), along with two lists \(a\) and \(b\). For each test case, it handles \(q\) queries, where each query involves finding an interpolated value based on the lists \(a\) and \(b\). After processing all queries for all test cases, it outputs the results of these queries.

