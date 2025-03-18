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
        
    #State: `data` is a list of strings; `idx` points to the position right after the last pair of `l` and `r` processed; `t` is 0; `results` is a list containing all results from all test cases, each test case contributing `q_i` results followed by an empty string; `n`, `q`, `a`, `pf`, and `mp` reflect the state of the last processed test case.
    print('\n'.join(results))
    #This is printed: Each result from the test cases, separated by newlines, with an empty line between results of different test cases
#Overall this is what the function does:The function `func_1` processes multiple test cases. Each test case includes an array `a` of `n` integers and `q` queries. Each query specifies a subarray using indices `l` and `r` (1-based indexing). The function determines whether there exists a subarray within the specified range `[l, r]` whose XOR is zero and appends 'YES' or 'NO' to the results based on this condition. After processing all test cases, it prints the results, separating them by newlines and inserting an empty line between results of different test cases.

