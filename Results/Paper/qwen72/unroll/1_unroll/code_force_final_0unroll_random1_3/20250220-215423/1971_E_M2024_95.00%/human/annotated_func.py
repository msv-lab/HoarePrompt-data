#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and q are integers where k ≤ n ≤ 10^9 and 1 ≤ k, q ≤ 10^5, representing the final destination, the number of known points, and the number of queries, respectively. a is a list of k integers where 1 ≤ a_i ≤ n and a_i < a_{i+1} for every 1 ≤ i ≤ k-1, with a_k = n. b is a list of k integers where 1 ≤ b_i ≤ 10^9 and b_i < b_{i+1} for every 1 ≤ i ≤ k-1. d is a list of q integers where 0 ≤ d ≤ n, representing the distances for which Timur wants to know the time. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
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
        
    #State: The loop processes each test case and for each query distance, it prints the corresponding time based on the calculated velocity and position. The variables `t`, `n`, `k`, `q`, `a`, `b`, `ad`, `bd`, `v`, and `ql` are updated and used within the loop, but their final values after the loop are not directly relevant to the output state. The output state is the printed result for each query distance, which is the time it takes to reach that distance.
#Overall this is what the function does:The function processes multiple test cases, each defined by parameters `n`, `k`, `q`, `a`, and `b`. For each test case, it reads a list of distances `d` from user input, and for each distance in `d`, it calculates and prints the time it takes to reach that distance based on the known points and times provided in `a` and `b`. The function does not return any value; it directly prints the results. After processing all test cases, the function concludes, and the final state includes the printed times for each query distance in each test case.

