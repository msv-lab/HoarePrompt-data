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
        
    #State: Output State: The output state consists of `t` lines, each containing `q` integers. For each test case, the integers represent the result of the query `m` calculated using the formula `m += b[s - 1] + bd[s] * (ql - a[s - 1]) / ad[s]` where `s` is determined by the position of `ql` in the list `a`. If `ql` is exactly equal to `a[s]`, the output is simply `b[s]`. The calculations are performed for each query `l` from `0` to `q-1` for each test case `t`.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( k \), and \( q \), along with lists \( a \) and \( b \). For each test case, it handles \( q \) queries, calculating a value \( m \) based on the position of the query value \( ql \) within the list \( a \). If \( ql \) matches an element in \( a \), the output is the corresponding element in \( b \). Otherwise, it interpolates the value using the differences between consecutive elements in \( a \) and \( b \). The function outputs the results of these queries for each test case.

