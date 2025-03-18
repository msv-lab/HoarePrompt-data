#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n, k, and q are integers such that k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, and the sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5. a is a strictly increasing list of k integers where each a_i satisfies 1 ≤ a_i ≤ n and a_k = n. b is a strictly increasing list of k integers where each b_i satisfies 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. d is an integer such that 0 ≤ d ≤ n.
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
        
    #State: After the loop executes all iterations, `i` is equal to `len(a)`, `v` is a list containing elements calculated as `ad[i] / bd[i]` for each `i` from 2 to `len(a) - 1`, `l` is equal to `q`, `m` is the cumulative value of `b[s - 1]` plus the sum of `bd[s] * (ql - a[s - 1]) / ad[s]` for each iteration, `q` is greater than or equal to 0, `s` is the index where `ql - a[s - 1]` would be inserted to keep the list `a` sorted, and if `a[s]` is equal to `ql - a[s - 1]`, no changes are made. If `a[s]` is not equal to `ql - a[s - 1]`, no changes are made either since there is no else part.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( t \), \( n \), \( k \), and \( q \). For each test case, it reads two lists \( a \) and \( b \), both strictly increasing. It then calculates intermediate values \( ad \) and \( bd \) based on differences between consecutive elements of \( a \) and \( b \), respectively. Using these values, it computes a series of cumulative sums \( m \) for given queries \( ql \). For each query, it finds the appropriate position in list \( a \) and calculates \( m \) using the corresponding values from \( b \) and \( ad \) and \( bd \). Finally, it prints the result for each query.

