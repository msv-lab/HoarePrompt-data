#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers where each element a_i satisfies 0 <= a_i < 2^30. Each query is defined by two integers l and r such that 1 <= l < r <= n. The sum of n across all test cases does not exceed 2 * 10^5, and the sum of q across all test cases does not exceed 2 * 10^5.
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
        
    #State: `data` is a list of strings split from the input line; `t` is an integer value greater than 0; `idx` is the final index pointing to the end of the `data` list; `results` is a list containing `q + 1` elements for each of the `t` iterations, where the first `q` elements are either `'YES'` or `'NO'`, and the last element is `''`.
    print('\n'.join(results))
    #This is printed: a series of 'YES' and 'NO' statements, each iteration ending with an empty line (where each iteration consists of q 'YES'/'NO' statements followed by an empty string)
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an array of integers and a series of queries. For each query, it determines whether there exists a subarray within the specified range whose XOR is zero. It outputs 'YES' if such a subarray exists and 'NO' otherwise, followed by an empty line after processing each test case.

