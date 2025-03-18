#State of the program right berfore the function call: The function should take parameters t, n, q, and a list of integers a, and a list of queries. t is an integer where 1 <= t <= 10^4, n and q are integers where 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5, a is a list of n integers where 0 <= a_i < 2^30, and each query is a pair of integers (l, r) where 1 <= l < r <= n. The sum of n over all test cases and the sum of q over all test cases do not exceed 2 * 10^5.
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
        
    #State: `idx` is `2 * (t + q * t)`, `results` is a list containing `t * q + t` strings where each string is either 'YES' or 'NO' followed by an empty string for each test case.
    print('\n'.join(results))
    #This is printed: [t * q + t lines of either 'YES' or 'NO' followed by an empty string]
#Overall this is what the function does:The function `func_1` processes a series of test cases, each containing a list of integers and a set of queries. For each query, it determines if there exists a subarray within the specified range whose XOR is zero. The function outputs a series of 'YES' or 'NO' responses for each query, followed by an empty line for each test case. The final state of the program includes the `idx` variable being `2 * (t + q * t)` and the `results` list containing `t * q + t` strings, where each string is either 'YES' or 'NO' followed by an empty string for each test case.

