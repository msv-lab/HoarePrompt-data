#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. Each test case consists of n and q where 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5. The array a is a list of n integers where 0 ≤ a_i < 2^{30}. Each query is defined by l and r where 1 ≤ l < r ≤ n.
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
        
    #State: `total` is 0, `t` is an integer value from `data[0]`, `results` is a list containing 'YES' or 'NO' for each query based on the conditions specified in the loop, `n` is an integer value from `data[2]` and must be greater than 4, `q` is 0, `a` is a list of length `n + 1` where each element from `a[1]` to `a[n+1]` is equal to `int(data[idx - n + i])` for `i` from 1 to `n + 1`, `pf` is a list of length `n + 1` where each element `pf[i]` is calculated as `pf[i-1] ^ a[i]` for `i` from 1 to `n + 1`, `mp` is a dictionary with keys being cumulative XOR results and values being lists of indices where these results occur in `a`, `i` is `n + 1`, `idx` is equal to the initial value plus the total number of elements in the list `a` multiplied by the number of iterations, `x` is `pf[r] ^ pf[l - 1]`, `v1` and `v2` are lists retrieved from `mp.get(pf[r], [])` and `mp.get(pf[l - 1], [])` respectively, and `it1` and `it2` are indices used to check the conditions for appending 'YES' or 'NO' to `results`; `results` now has an empty string appended to it.
    print('\n'.join(results))
    #This is printed: '\n'.join(results) (where results is a list of 'YES' or 'NO' based on certain conditions specified in the loop)
#Overall this is what the function does:The function processes multiple test cases, each containing an integer t, followed by arrays n and q, and an array a. For each test case, it handles q queries, each defined by indices l and r. It calculates the result for each query based on the XOR values of the subarray from index l to r, and appends 'YES' or 'NO' to the results list accordingly. Finally, it prints the results list, which contains 'YES' or 'NO' for each query.

