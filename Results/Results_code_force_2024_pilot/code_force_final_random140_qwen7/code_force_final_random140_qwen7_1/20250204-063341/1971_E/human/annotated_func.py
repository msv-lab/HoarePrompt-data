#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and q are integers such that k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, and the sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5. a is a strictly increasing list of k integers where 1 ≤ a_i ≤ n and a_i < a_{i+1} for every 1 ≤ i ≤ k-1, and a_k = n. b is a strictly increasing list of k integers where 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. Each query d is an integer such that 0 ≤ d ≤ n.
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
            m += bd[s] * ql // ad[s]
            print(m, end=' ')
        
        print()
        
    #State: Output State: All variables will reach their final state after all iterations of the loop have completed.
    #
    #After all iterations of the loop have finished, the following conditions will be true:
    #
    #- `i` will be equal to `len(b)`, indicating that the loop has processed all elements in the list `b`.
    #- `q` will be reduced to `0` after all queries have been processed.
    #- `v` will contain the ratio of differences between consecutive elements in `a` and `b` for all valid indices, starting from the second element of both lists.
    #- `m` will be the cumulative sum of `b[s-1]` for all `s` from `1` to `len(b) - 1`, plus the sum of `bd[s] * (ql - a[s - 1])` for all `s` from `1` to `len(b) - 1`, reflecting the final accumulated value after processing all queries.
    #- `l` will be `0` since all queries have been processed.
    #- `ql` will be `0` as it gets reduced to zero after processing all queries.
    #- `s` will be the final index where `ql` would be inserted to keep the list `a` sorted, but since `ql` is `0`, this index will be the last position in the list `a`.
    #
    #In summary, after all iterations, `i` and `l` will be `len(b)` and `0`, respectively, while `q` will be `0`. The values of `v`, `m`, `ql`, and `s` will reflect the final state after processing all inputs and queries.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, k, q, lists a and b, and a series of queries d. For each query d, it calculates and prints a corresponding value based on the differences between consecutive elements in lists a and b. After processing all queries for all test cases, the function outputs the final results.

