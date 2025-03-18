#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers where each element a_i satisfies 0 <= a_i < 2^30. Each query is defined by two integers l and r such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5, and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: - `t` remains unchanged as it is the number of test cases.
    #   - `n` and `q` are the last values read from `data` during the last iteration.
    #   - `a` and `pf` are the arrays computed during the last iteration.
    #   - `mp` is the dictionary computed during the last iteration.
    #   - `idx` is the index after processing all test cases.
    #   - `results` contains the results of all queries for all test cases, ending with an empty string for each test case.
    #
    #Given the above analysis, the final output state can be described as:
    #
    #Output State:
    print('\n'.join(results))
    #This is printed: query_result_1\nquery_result_2\n...\n\nquery_result_x\nquery_result_y\n...\n (where each query_result is the result of a query and newlines separate the results of different queries and test cases)
#Overall this is what the function does:The function processes multiple test cases, each consisting of an array and a set of queries. For each query, it determines if there exists a subarray within the specified range whose XOR is zero. The results for all queries across all test cases are printed, with each test case's results separated by a newline.

