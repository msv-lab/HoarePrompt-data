#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. Each test case consists of two integers n and q where 2 ≤ n ≤ 2 · 10^5 and 1 ≤ q ≤ 2 · 10^5, representing the number of elements in the array and the number of queries, respectively. The array a contains n integers a_1, ..., a_n where 0 ≤ a_i < 2^30. Each query is represented by two integers l and r where 1 ≤ l < r ≤ n. The sum of n over all test cases and the sum of q over all test cases do not exceed 2 · 10^5.
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
        
    #State: After the loop has executed all iterations, `idx` will be `3 + t * (n + 2 * q + 2)`, `results` will contain 'YES' or 'NO' for each query based on the conditions evaluated in the loop, followed by `t` empty strings at the end. The variables `t`, `data`, `n`, `q`, `a`, `pf`, and `mp` will remain unchanged for each iteration but will be reset for the next test case.
    print('\n'.join(results))
    #This is printed: 'YES' or 'NO' for each query, followed by `t` empty lines
#Overall this is what the function does:The function `func_1` processes a series of test cases, each containing an array of integers and a set of queries. It reads the input data, which includes the number of test cases, the size of the array, the array itself, and the queries. For each query, it determines whether the XOR of the elements in the specified subarray is zero or if there exists a pair of indices within the subarray that have the same prefix XOR value. The function outputs 'YES' if either condition is met, otherwise 'NO'. The output for each test case is followed by an empty line.

