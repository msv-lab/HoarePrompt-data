#State of the program right berfore the function call: t is a positive integer (1 ≤ t ≤ 10^4), representing the number of test cases. For each test case, n, k, and q are integers where k ≤ n ≤ 10^9, 1 ≤ k, q ≤ 10^5, representing the final destination, the number of known time points, and the number of queries, respectively. a is a list of k integers (1 ≤ a_i ≤ n, a_i < a_{i+1}, a_k = n), representing the positions of the signs. b is a list of k integers (1 ≤ b_i ≤ 10^9, b_i < b_{i+1}), representing the times when the car arrives at the corresponding positions in a. Each of the q queries is an integer d (0 ≤ d ≤ n), representing the distance for which Timur wants to know the travel time. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
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
        
    #State: After all iterations of the loop, `l` will be equal to `q - 1`, `m` will have been updated to `b[s - 1] + bd[s] * (ql - a[s - 1]) // ad[s]` for each query `ql` where `a[s] != ql`, and `ql` will have been adjusted to `ql - a[s - 1]` for each query. The index `s` will hold the position where the current `ql` fits in the list `a` to maintain the order. The variables `a`, `ad`, `b`, `bd`, and `v` will remain unchanged from their initial states.
#Overall this is what the function does:The function processes multiple test cases, each defined by parameters `n`, `k`, `q`, `a`, and `b`. For each test case, it calculates and prints the travel time for each of the `q` queries. The travel times are determined based on the positions and arrival times specified in the lists `a` and `b`. The function reads input values from standard input and prints the results to standard output. After processing all test cases, the function completes without returning any value. The state of the program remains unchanged except for the printed output.

