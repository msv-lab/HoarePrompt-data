#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n and q are integers such that 2 <= n <= 2 * 10^5 and 1 <= q <= 2 * 10^5. The array a contains n integers where each element a_i satisfies 0 <= a_i < 2^30. For each query, l and r are integers such that 1 <= l < r <= n. The sum of n over all test cases does not exceed 2 * 10^5 and the sum of q over all test cases does not exceed 2 * 10^5.
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
        
    #State: data is a list of strings representing the input values; t is 0; idx is the final index after processing all test cases; n and q are the values from the last test case processed; a is the list of integers from the last test case; pf is the prefix XOR list from the last test case; mp is the dictionary of prefix XOR values and their indices from the last test case; results is a list of 'YES' or 'NO' based on the conditions checked in each iteration of the loop for all test cases, and it includes an additional empty string after the results of the last test case.
    print('\n'.join(results))
    #This is printed: 'YES\nNO\n...\n' (where each 'YES' or 'NO' corresponds to the result of each test case, and there is an additional newline at the end)
#Overall this is what the function does:The function `func_1` processes multiple test cases, each consisting of an array `a` and a series of queries. For each query, it determines if there exists a subarray within the specified range `[l, r]` such that the XOR of its elements is zero. It outputs 'YES' if such a subarray exists and 'NO' otherwise, followed by a newline after processing all queries of a test case.

