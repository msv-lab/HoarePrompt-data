#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n, k, and q are integers where 1 ≤ k ≤ n ≤ 10^9 and 1 ≤ k, q ≤ 10^5. The lists a and b are strictly increasing sequences of integers, with a_i and b_i such that 1 ≤ a_i ≤ n and 1 ≤ b_i ≤ 10^9 for all i, and a_k = n. Each query d is an integer such that 0 ≤ d ≤ n. The sum of k over all test cases does not exceed 10^5, and the sum of q over all test cases does not exceed 10^5.
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
        
    #State: The loop processes all test cases and prints the results for each query. The variables t, n, k, q, a, b, ad, bd, v, and m are modified within the loop for each test case, but their final values are not retained between test cases. After all iterations, t is 0 (as all test cases have been processed), and the lists a, b, ad, bd, and v are reset to their initial states for each new test case. The variable m is reset to 0 for each query within a test case. The final output state is the same as the initial state, except that all test cases and queries have been processed and the corresponding results have been printed.
#Overall this is what the function does:The function `func` processes multiple test cases, each defined by integers `n`, `k`, and `q`, and two strictly increasing sequences of integers `a` and `b`. For each test case, it reads the sequences `a` and `b`, and for each query `d` (where `0 ≤ d ≤ n`), it computes and prints the corresponding value from `b` or an interpolated value based on the sequences `a` and `b`. After processing all test cases, the function does not return any value; it only prints the results of the queries. The final state of the program is such that all test cases and queries have been processed, and the results have been printed to the console.

