#State of the program right berfore the function call: t is a positive integer, each test case consists of n and q where 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5, a is a list of n integers where 0 ≤ a_i < 2^{30}, and each query consists of two integers l and r where 1 ≤ l < r ≤ n.
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
        
    #State: `idx` is 2, `t` is an integer derived from `data[0]`, `data` is a list of strings representing the split input, n and q are integers derived from the input, a is a list of n integers, and each query consists of two integers l and r where 1 ≤ l < r ≤ n; `results` is a list containing 'YES' or 'NO' for each query followed by an empty string.
    print('\n'.join(results))
    #This is printed: YES\nNO\nYES\nNO\n... (each 'YES' or 'NO' followed by a newline, ending with an empty line)
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `t`, a list `a` of `n` integers, and `q` queries. For each query, it checks if the given indices `l` and `r` (where `1 ≤ l < r ≤ n`) are valid. If valid, it computes the XOR of the sublist of `a` from index `l-1` to `r-1`. If the result of this XOR operation is zero, it appends 'YES' to the results; otherwise, it appends 'NO'. If the indices are invalid, it handles this case accordingly. After processing all queries for each test case, it appends an empty string to the results. Finally, it prints the results, which consist of 'YES' or 'NO' for each query followed by an empty line.

