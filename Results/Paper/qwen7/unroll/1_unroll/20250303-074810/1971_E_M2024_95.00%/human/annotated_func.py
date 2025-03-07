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
            m += bd[s] * ql / ad[s]
            print(int(m), end=' ')
        
        print()
        
    #State: Output State: The output state will consist of a series of integers printed for each query within each test case. For each test case, there will be `q` lines of output, where each line contains the result of a query. Each query involves finding the interpolated value between two points defined by arrays `a` and `b`, based on the position `ql` provided in the query. The interpolated value is calculated using the differences in `a` and `b` arrays and printed as an integer. This process is repeated for `t` test cases.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers n, k, q, and lists a and b. For each test case, it handles q queries, where each query provides an integer d. The function calculates and prints the interpolated value between two points in the lists a and b based on the position d for each query. The interpolated value is determined using the differences in elements of lists a and b, and the results are printed as integers. This process is repeated for all test cases.

