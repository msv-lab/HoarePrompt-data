#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4; for each test case, n and q are integers such that 2 ≤ n ≤ 2⋅10^5 and 1 ≤ q ≤ 2⋅10^5; a is a list of n integers such that 0 ≤ a_i < 2^{30}; for each query, l and r are integers such that 1 ≤ l < r ≤ n.
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
        
    #State: Output State: `idx` is 6, `t` is an integer equal to `int(data[0])`, `results` is a list containing 'NO' repeated `q * (t - 1)` times followed by an empty string.
    #
    #Explanation: The loop iterates `t` times, and each iteration processes `n` elements and `q` queries. After processing all `t` iterations, the index `idx` will be incremented by `2 * t` (2 for each iteration), resulting in `idx` being 6. The `results` list will contain `q * (t - 1)` 'NO' responses followed by one empty string, as no conditions for 'YES' were met in the given code snippet.
    print('\n'.join(results))
    #This is printed: NO\nNO\n... (2q times)\n
#Overall this is what the function does:The function processes multiple test cases, where each test case includes an integer `t`, followed by `n` and `q` integers, a list `a` of `n` integers, and `q` queries. Each query consists of two integers `l` and `r`. For each test case, the function checks if there exists a subarray within the range `[l, r]` whose bitwise XOR is zero. If such a subarray is found, the result for that query is 'YES'; otherwise, it is 'NO'. The function then prints the results for all queries in the order they were processed, followed by an empty line.

