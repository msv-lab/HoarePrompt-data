#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers where each element a_i satisfies 0 <= a_i < 2^30. Each query is defined by two integers l and r such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5 and the sum of q over all test cases does not exceed 2 * 10^5.
def func_1():
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        q = int(data[idx + 1])
        
        idx += 2
        
        a = [0] * (n + 1)
        
        pf = [0] * (n + 1)
        
        mp = {(0): [0]}
        
        for i in range(1, n + 1):
            a[i] = int(data[idx])
            idx += 1
            pf[i] = pf[i - 1] ^ a[i]
            if pf[i] not in mp:
                mp[pf[i]] = []
            mp[pf[i]].append(i)
        
        for _ in range(q):
            l = int(data[idx])
            r = int(data[idx + 1])
            idx += 2
            x = pf[r] ^ pf[l - 1]
            if x == 0:
                results.append('YES')
                continue
            v1 = mp.get(pf[r], [])
            v2 = mp.get(pf[l - 1], [])
            it1 = bisect.bisect_left(v1, l)
            it2 = bisect.bisect_left(v2, r) - 1
            if it1 < len(v1) and it2 >= 0 and v1[it1] <= r and v2[it2] >= l:
                results.append('YES')
            else:
                results.append('NO')
        
        results.append('')
        
    #State: `t` is an integer such that 1 <= t <= 10^4; `n` and `q` are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5; `data` is a list of strings representing the input values; `a` and `queries` are not yet processed; `idx` is equal to 1 + 2*t + n*q (the index after processing all test cases); `results` is a list containing the answers to all the queries, with each test case's results followed by an empty string.
    print('\n'.join(results))
    #This is printed: [Each element of results on a new line, with an additional newline separating the results of different test cases]
#Overall this is what the function does:The function processes multiple test cases. Each test case includes an array of integers and a series of queries. For each query, it determines if there exists a subarray within the specified range that has a bitwise XOR of zero and returns "YES" if such a subarray exists, otherwise "NO". The results for all queries in a test case are printed together, with an empty line separating the results of different test cases.

