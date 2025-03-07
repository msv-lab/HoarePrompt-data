#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of two integers n and q such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. The next line contains n integers a_1,...,a_n such that 0 ≤ a_i < 2^{30}. Each query is described by two integers l and r such that 1 ≤ l < r ≤ n.
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
        
    #State: Output State: `idx` is equal to `2 * n + 1`, `t` is decremented by 3, `results` is a list of length `q * 3` containing the outcomes ('YES' or 'NO') of the conditions checked in each iteration of the loop, and an empty string is appended to `results`.
    #
    #In natural language: After the loop executes all its iterations, `idx` will be set to `2 * n + 1`, indicating that all elements in the `data` list up to the current `idx` have been processed. The variable `t` will be reduced by 3 because the loop runs for `t` iterations, and in this case, `t` has completed 3 full iterations. The `results` list will contain the outcomes of the conditions checked in each of the three iterations, followed by an additional empty string.
    print('\n'.join(results))
    #This is printed: YES\nNO\nYES\n\n
#Overall this is what the function does:The function processes multiple test cases, where each test case includes an integer t, followed by integers n and q, and a list of n integers a_1,...,a_n. For each query (l, r) given within a test case, the function determines if the subarray a_l,...,a_r contains a contiguous subsequence with a bitwise XOR of 0. If such a subsequence exists, the function appends 'YES' to the results; otherwise, it appends 'NO'. After processing all queries for a test case, an empty string is appended to the results. This process repeats for each test case, and the final output is a list of 'YES' and 'NO' values, one for each query, followed by an empty string for each test case.

