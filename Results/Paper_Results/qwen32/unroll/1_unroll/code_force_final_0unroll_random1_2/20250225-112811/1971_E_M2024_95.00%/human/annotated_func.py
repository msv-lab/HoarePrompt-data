#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n, k, and q are integers such that k <= n <= 10^9, 1 <= k, q <= 10^5. a is a list of k integers where 1 <= a_i <= n, a_i < a_{i+1} for every 1 <= i <= k-1, and a_k = n. b is a list of k integers where 1 <= b_i <= 10^9, b_i < b_{i+1} for every 1 <= i <= k-1. For each of the q queries, d is an integer such that 0 <= d <= n. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
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
        
    #State: The output state consists of the results of q queries for each of the t test cases. For each query d, the output is either the value b[s] if d matches an element a[s] in list a, or the calculated interpolated value m based on the differences in lists a and b. The final output for each test case is a line of space-separated results for each query, followed by a newline character.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two sorted lists `a` and `b`, and a series of queries. For each query, it determines the corresponding value from list `b` either directly if the query matches an element in list `a`, or by linear interpolation based on the differences between consecutive elements in `a` and `b`. The results of all queries for a test case are printed on a single line, separated by spaces.

