#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers where each integer a_i satisfies 0 <= a_i < 2^30. Each query is defined by two integers l and r such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5, and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: results is a list containing the results of all queries for each test case, followed by an empty string for each test case. `data`, `t`, and `idx` remain unchanged from their initial values except `idx` which will point past the last element processed.
    print('\n'.join(results))
    #This is printed: Result1\nResult2\n\nResult3\nResult4\n
#Overall this is what the function does:The function `func_1` processes multiple test cases, where each test case consists of an array `a` of `n` integers and `q` queries. Each query asks whether there exists a subarray within the specified range `[l, r]` such that the XOR of all its elements is zero. The function outputs "YES" if such a subarray exists and "NO" otherwise, for each query. The results for each test case are printed sequentially, with an empty line separating the results of different test cases.

